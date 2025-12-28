# day 10

# Referenced this reddit: https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

import re
from collections import deque
from functools import lru_cache

LINE_RE = re.compile(r"\[([.#]+)\]")
CURLY_RE = re.compile(r"\{([^}]*)\}")

def parse_line(line: str):
    m = LINE_RE.search(line)
    diagram = m.group(1)
    n = len(diagram)

    target = 0
    for i, ch in enumerate(diagram):
        if ch == "#":
            target |= (1 << i)

    btn_strs = re.findall(r"\(([^)]*)\)", line)
    buttons = []
    for bs in btn_strs:
        bs = bs.strip()
        if not bs:
            continue
        idxs = [int(x.strip()) for x in bs.split(",") if x.strip() != ""]
        mask = 0
        for k in idxs:
            mask |= (1 << k)
        buttons.append(mask)

    return n, target, buttons

def min_presses(n: int, target: int, buttons) -> int:
    start = 0
    if start == target:
        return 0

    dist = {start: 0}
    q = deque([start])

    while q:
        state = q.popleft()
        d = dist[state]
        nd = d + 1
        for b in buttons:
            nxt = state ^ b
            if nxt not in dist:
                dist[nxt] = nd
                if nxt == target:
                    return nd
                q.append(nxt)

    return None

def parse_line2(line: str):
    btn_strs = re.findall(r"\(([^)]*)\)", line)
    buttons = []
    for bs in btn_strs:
        bs = bs.strip()
        if not bs:
            continue

        idxs = [int(x.strip()) for x in bs.split(",") if x.strip() != ""]
        buttons.append(idxs)

    m = CURLY_RE.search(line)
    reqs = [int(x.strip()) for x in m.group(1).split(",") if x.strip() != ""]

    return len(reqs), reqs, buttons

def min_presses_joltage(reqs, buttons) -> int:
    reqs = tuple(reqs)
    m = len(reqs)

    cleaned = []
    seen = set()
    for idxs in buttons:
        s = tuple(sorted({i for i in idxs if 0 <= i < m}))

        if s and s not in seen:
            seen.add(s)
            cleaned.append(s)

    btns = cleaned

    if not btns:
        return 0 if all(r == 0 for r in reqs) else None

    hit = [False] * m

    for b in btns:
        for i in b:
            hit[i] = True

    for i, r in enumerate(reqs):
        if r > 0 and not hit[i]:
            return None

    parity_masks = []
    for b in btns:
        pm = 0
        for i in b:
            pm |= (1 << i)
        parity_masks.append(pm)

    desired_parity_mask = 0

    for i, r in enumerate(reqs):
        if r & 1:
            desired_parity_mask |= (1 << i)

    B = len(btns)

    @lru_cache(maxsize=None)
    def f(state):
        if all(v == 0 for v in state):
            return 0

        if any(v < 0 for v in state):
            return 10 ** 18

        want = 0
        for i, v in enumerate(state):
            if v & 1:
                want |= (1 << i)

        best = 10 ** 18
        counts = [0] * m

        def dfs(j, cur_parity, presses_so_far):
            nonlocal best

            if presses_so_far >= best:
                return

            if j == B:
                if cur_parity != want:
                    return

                nxt = []
                for i in range(m):
                    rem = state[i] - counts[i]
                    nxt.append(rem // 2)

                rec = f(tuple(nxt))
                if rec >= 10 ** 18:
                    return
                cand = presses_so_far + 2 * rec
                if cand < best:
                    best = cand
                return

            dfs(j + 1, cur_parity, presses_so_far)

            b = btns[j]

            for i in b:
                if counts[i] + 1 > state[i]:
                    break
            else:
                # apply
                for i in b:
                    counts[i] += 1
                dfs(j + 1, cur_parity ^ parity_masks[j], presses_so_far + 1)
                # undo
                for i in b:
                    counts[i] -= 1

        dfs(0, 0, 0)
        return best

    ans = f(reqs)
    return None if ans >= 10 ** 18 else ans

total = 0
total2 = 0

with open("inputs/day10.txt") as f:
    for raw in f:
        line = raw.strip()
        if not line:
            continue
        n, target, buttons = parse_line(line)
        ans = min_presses(n, target, buttons)
        total += ans

        m, reqs, btns2 = parse_line2(line)
        ans2 = min_presses_joltage(reqs, btns2)
        total2 += ans2

print(total)
print(total2)