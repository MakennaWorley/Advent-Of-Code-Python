# day 9
from collections import deque

def parse_points(text: str):
    pts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        pts.append((x, y))
    return pts

def max_rectangle_area(points) -> int:
    best = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area > best:
                best = area

    return best

def build_path_segments(points):
    segs = []
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if x1 == x2:
            ya, yb = sorted((y1, y2))
            segs.append(("V", x1, ya, yb))

        elif y1 == y2:
            xa, xb = sorted((x1, x2))
            segs.append(("H", y1, xa, xb))

    return segs

def compress_coords(points):
    xs = set()
    ys = set()
    for x, y in points:
        xs.add(x); xs.add(x - 1); xs.add(x + 1)
        ys.add(y); ys.add(y - 1); ys.add(y + 1)

    xs = sorted(xs)
    ys = sorted(ys)

    x_idx = {x:i for i, x in enumerate(xs)}
    y_idx = {y:i for i, y in enumerate(ys)}

    xw = [xs[i+1] - xs[i] for i in range(len(xs) - 1)]
    yh = [ys[i+1] - ys[i] for i in range(len(ys) - 1)]

    return xs, ys, x_idx, y_idx, xw, yh

def mark_boundary(points, xs, ys, x_idx, y_idx):
    W = len(xs) - 1
    H = len(ys) - 1
    boundary = [[0] * W for _ in range(H)]

    segs = build_path_segments(points)

    for kind, a, b0, b1 in segs:
        if kind == "V":
            x = a
            ya, yb = b0, b1
            xi = x_idx[x]
            cx = max(0, min(W - 1, xi - 1))

            y_start = y_idx[ya]
            y_end = y_idx[yb]
            if y_start > y_end:
                y_start, y_end = y_end, y_start

            for cy in range(y_start, y_end):
                boundary[cy][cx] = 1

        else:
            y = a
            xa, xb = b0, b1
            yi = y_idx[y]
            cy = max(0, min(H - 1, yi - 1))

            x_start = x_idx[xa]
            x_end = x_idx[xb]
            if x_start > x_end:
                x_start, x_end = x_end, x_start

            for cx in range(x_start, x_end):
                boundary[cy][cx] = 1

    return boundary

def fill_allowed(boundary):
    H = len(boundary)
    W = len(boundary[0])

    outside = [[0] * W for _ in range(H)]
    q = deque()

    for x in range(W):
        if boundary[0][x] == 0:
            outside[0][x] = 1; q.append((0, x))

        if boundary[H-1][x] == 0:
            outside[H-1][x] = 1; q.append((H-1, x))

    for y in range(H):
        if boundary[y][0] == 0:
            outside[y][0] = 1; q.append((y, 0))

        if boundary[y][W-1] == 0:
            outside[y][W-1] = 1; q.append((y, W-1))

    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < H and 0 <= nx < W):
                continue

            if outside[ny][nx]:
                continue

            if boundary[ny][nx]:
                continue

            outside[ny][nx] = 1
            q.append((ny, nx))

    allowed = [[0] * W for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if outside[y][x] == 0:
                allowed[y][x] = 1

    return allowed

def prefix2(grid):
    H = len(grid)
    W = len(grid[0])
    ps = [[0] * (W + 1) for _ in range(H + 1)]

    for y in range(1, H + 1):
        row = 0
        for x in range(1, W + 1):
            row += grid[y-1][x-1]
            ps[y][x] = ps[y-1][x] + row

    return ps

def rect_sum(ps, y0, x0, y1, x1):
    y0 += 1; x0 += 1; y1 += 1; x1 += 1
    return ps[y1][x1] - ps[y0-1][x1] - ps[y1][x0-1] + ps[y0-1][x0-1]

def build_area_prefix(xw, yh):
    px = [0]

    for w in xw:
        px.append(px[-1] + w)

    py = [0]

    for h in yh:
        py.append(py[-1] + h)

    return px, py

def span_sum(p, a, b):
    return p[b+1] - p[a]

def max_rectangle(points):
    xs, ys, x_idx, y_idx, xw, yh = compress_coords(points)

    boundary = mark_boundary(points, xs, ys, x_idx, y_idx)
    allowed = fill_allowed(boundary)

    H = len(allowed)
    W = len(allowed[0])

    red = set()
    for x, y in points:
        xi = x_idx[x]
        yi = y_idx[y]
        cx = max(0, min(W - 1, xi))
        cy = max(0, min(H - 1, yi))
        red.add((cy, cx))

    ps_allowed = prefix2(allowed)
    px, py = build_area_prefix(xw, yh)

    best = 0

    red_list = list(red)
    n = len(red_list)

    for i in range(n):
        y1, x1 = red_list[i]
        for j in range(i + 1, n):
            y2, x2 = red_list[j]
            if x1 == x2 or y1 == y2:
                continue

            ya, yb = (y1, y2) if y1 < y2 else (y2, y1)
            xa, xb = (x1, x2) if x1 < x2 else (x2, x1)

            cells = (yb - ya + 1) * (xb - xa + 1)
            if rect_sum(ps_allowed, ya, xa, yb, xb) != cells:
                continue

            true_w = span_sum(px, xa, xb)
            true_h = span_sum(py, ya, yb)
            area = true_w * true_h

            if area > best:
                best = area

    return best

with open("inputs/day9.txt") as f:
    points = parse_points(f.read())

print(max_rectangle_area(points))
print(max_rectangle(points))