# day 8
from collections import Counter

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.sz = [1] * n
        self.components = n

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]

        return a

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra

        self.sz[ra] += self.sz[rb]
        self.components -= 1

        return True

def parse_points(text: str):
    pts = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        x, y, z = map(int, line.split(","))
        pts.append((x, y, z))

    return pts

def dist2(a, b) -> int:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]

    return dx*dx + dy*dy + dz*dz

def solve(points, k_edges: int = 1000) -> int:
    n = len(points)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((dist2(points[i], points[j]), i, j))

    edges.sort(key=lambda t: t[0])

    dsu = DSU(n)

    k = min(k_edges, len(edges))
    for idx in range(k):
        _, a, b = edges[idx]
        dsu.union(a, b)

    roots = [dsu.find(i) for i in range(n)]
    counts = Counter(roots)
    sizes = sorted(counts.values(), reverse=True)

    return sizes[0] * sizes[1] * sizes[2]

def solve2(points) -> int:
    n = len(points)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((dist2(points[i], points[j]), i, j))

    edges.sort(key=lambda t: t[0])

    dsu = DSU(n)

    last_edge = None
    for _, a, b in edges:
        if dsu.union(a, b):
            last_edge = (a, b)
            if dsu.components == 1:
                break

    a, b = last_edge
    return points[a][0] * points[b][0]

with open("inputs/day8.txt") as f:
    points = parse_points(f.read())

print(solve(points, 1000))
print(solve2(points))