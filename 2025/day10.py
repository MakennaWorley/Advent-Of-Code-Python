# day 10
import re
import heapq
from collections import deque

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

    return reqs, buttons

def min_presses_joltage(reqs, buttons) -> int:
    m = len(reqs)

    btns = []
    for idxs in buttons:
        s = tuple(sorted(set(i for i in idxs if 0 <= i < m)))
        if s:
            btns.append(s)

    btns = list(set(btns))  # dedupe
    if not btns:
        return 0 if all(r == 0 for r in reqs) else None

    for i, r in enumerate(reqs):
        if r > 0 and not any(i in b for b in btns):
            return None

    btns.sort(key=len, reverse=True)

    btn_sets = [set(b) for b in btns]
    filtered = []
    for i, b in enumerate(btn_sets):
        if any(i != j and b.issubset(btn_sets[j]) for j in range(len(btns))):
            continue
        filtered.append(btns[i])
    btns = filtered

    max_hit = max(len(b) for b in btns)

    start = tuple(reqs)
    if all(v == 0 for v in start):
        return 0

    def h(state):
        mx = max(state)
        sm = sum(state)
        return max(mx, (sm + max_hit - 1) // max_hit)

    pq = [(h(start), 0, start)]
    best = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)
        if g != best.get(state):
            continue
        if all(v == 0 for v in state):
            return g

        for b in btns:
            # apply press
            ns = list(state)
            changed = False
            for i in b:
                if ns[i] > 0:
                    ns[i] -= 1
                    changed = True
            if not changed:
                continue

            ns = tuple(ns)
            ng = g + 1
            if ng < best.get(ns, 10**18):
                best[ns] = ng
                heapq.heappush(pq, (ng + h(ns), ng, ns))

    return None

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

print(total)
print(total2)