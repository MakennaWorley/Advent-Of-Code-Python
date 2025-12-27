# day 12
from functools import lru_cache

def parse(text: str):
    lines = [ln.rstrip("\n") for ln in text.splitlines()]
    shapes = {}
    regions = []

    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        if not ln:
            i += 1
            continue

        if "x" in ln and ":" in ln and ln.split(":", 1)[0].count("x") == 1:
            break

        if ln.endswith(":") and ln[:-1].isdigit():
            idx = int(ln[:-1])
            i += 1
            grid = []

            while i < len(lines) and lines[i].strip() != "":
                grid.append(lines[i].strip())
                i += 1

            shapes[idx] = grid

        i += 1

    while i < len(lines):
        ln = lines[i].strip()
        i += 1
        if not ln:
            continue

        wh, counts_str = ln.split(":", 1)
        w_str, h_str = wh.split("x")
        w, h = int(w_str), int(h_str)
        counts = [int(x) for x in counts_str.strip().split()]
        regions.append((w, h, counts))

    max_idx = max(shapes) if shapes else -1
    shape_list = []

    for k in range(max_idx + 1):
        shape_list.append(shapes[k])

    return shape_list, regions

def shape_cells(shape_grid):
    pts = []
    for y, row in enumerate(shape_grid):
        for x, ch in enumerate(row):
            if ch == "#":
                pts.append((x, y))

    return pts


def normalize(pts):
    minx = min(x for x, y in pts)
    miny = min(y for x, y in pts)
    pts2 = sorted((x - minx, y - miny) for x, y in pts)
    return tuple(pts2)

def rotate90(pts):
    return [(y, -x) for x, y in pts]

def flip_x(pts):
    return [(-x, y) for x, y in pts]

def unique_orientations(shape_grid):
    base = shape_cells(shape_grid)
    seen = set()
    out = []

    pts = base[:]
    for _ in range(4):
        for f in (False, True):
            cur = flip_x(pts) if f else pts
            norm = normalize(cur)

            if norm not in seen:
                seen.add(norm)
                out.append(norm)

        pts = rotate90(pts)

    return out

def placement_masks(W, H, orient):
    maxx = max(x for x, y in orient)
    maxy = max(y for x, y in orient)
    masks = []

    for oy in range(H - maxy):
        for ox in range(W - maxx):
            m = 0
            for x, y in orient:
                gx = ox + x
                gy = oy + y
                bit = gy * W + gx
                m |= 1 << bit

            masks.append(m)

    return masks

def can_fit_region(W, H, shape_orients, counts):
    n_shapes = len(shape_orients)

    cell_counts = [len(shape_orients[s][0]) if shape_orients[s] else 0 for s in range(n_shapes)]
    total_area = 0
    for s in range(n_shapes):
        total_area += counts[s] * cell_counts[s]

    if total_area > W * H:
        return False

    placements = []
    for s in range(n_shapes):
        ms = []
        for orient in shape_orients[s]:
            ms.extend(placement_masks(W, H, orient))

        placements.append(ms)

    counts0 = tuple(counts)

    @lru_cache(None)
    def dfs(occ, remaining):
        if all(c == 0 for c in remaining):
            return True

        best_s = None
        best_opts = None
        best_len = 10**18

        for s, c in enumerate(remaining):
            if c == 0:
                continue

            opts = []

            for m in placements[s]:
                if (m & occ) == 0:
                    opts.append(m)

            if not opts:
                return False

            if len(opts) < best_len:
                best_len = len(opts)
                best_s = s
                best_opts = opts

                if best_len == 1:
                    break

        rem_list = list(remaining)
        rem_list[best_s] -= 1
        rem_next = tuple(rem_list)

        for m in best_opts:
            if dfs(occ | m, rem_next):
                return True

        return False

    return dfs(0, counts0)


def solve(text: str):
    shape_list, regions = parse(text)

    shape_orients = [unique_orientations(g) for g in shape_list]

    good = 0
    for W, H, counts in regions:
        if can_fit_region(W, H, shape_orients, counts):
            good += 1

    return good

with open("inputs/day12.txt") as f:
    text = f.read()

print(solve(text))
