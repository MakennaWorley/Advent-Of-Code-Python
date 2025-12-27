# day 11
from functools import lru_cache

def parse(text: str):
    edges = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        name, rest = line.split(":", 1)
        outs = rest.strip().split() if rest.strip() else []
        edges[name.strip()] = outs

    return edges

def count_paths(edges, start="you", target="out"):
    visiting = set()

    @lru_cache(None)
    def dfs(node: str) -> int:
        if node == target:
            return 1

        if node not in edges:
            return 0

        visiting.add(node)

        total = 0
        for nxt in edges[node]:
            total += dfs(nxt)

        visiting.remove(node)
        return total

    return dfs(start)

def count_paths_with_both(edges, start="svr", target="out"):
    visiting = set()

    @lru_cache(None)
    def dfs(node: str, seen1: int, seen2: int) -> int:
        if node == "dac":
            seen1 = 1
        if node == "fft":
            seen2 = 1

        if node == target:
            return 1 if (seen1 and seen2) else 0

        if node not in edges:
            return 0

        state = (node, seen1, seen2)
        visiting.add(state)

        total = 0
        for nxt in edges[node]:
            total += dfs(nxt, seen1, seen2)

        visiting.remove(state)
        return total

    return dfs(start, 0, 0)

with open("inputs/day11.txt") as f:
    text = f.read().strip()

edges = parse(text)
print(count_paths(edges, "you", "out"))
print(count_paths_with_both(edges, "svr", "out"))