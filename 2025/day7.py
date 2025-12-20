# day 7
from collections import defaultdict

def count_splits(grid_text: str) -> int:
    lines = [list(row.rstrip("\n")) for row in grid_text.splitlines() if row.strip("\n") != ""]
    rows, cols = len(lines), len(lines[0])

    sx, sy = None, None
    for y in range(rows):
        for x in range(cols):
            if lines[y][x] == "S":
                sx, sy = x, y
                break

        if sx is not None:
            break

    beams = {sx}
    splits = 0

    for y in range(sy + 1, rows):
        next_beams = set()

        for x in beams:
            if not (0 <= x < cols):
                continue

            cell = lines[y][x]

            if cell == "^":
                splits += 1
                next_beams.add(x - 1)
                next_beams.add(x + 1)
            else:
                next_beams.add(x)

        beams = next_beams

        if beams and all(x < 0 or x >= cols for x in beams):
            break

    return splits

def count_timelines(grid_text: str) -> int:
    lines = [list(row.rstrip("\n")) for row in grid_text.splitlines() if row.strip("\n") != ""]
    rows, cols = len(lines), len(lines[0])

    sx, sy = None, None
    for y in range(rows):
        for x in range(cols):
            if lines[y][x] == "S":
                sx, sy = x, y
                break

        if sx is not None:
            break

    beams = defaultdict(int)
    beams[sx] = 1
    exited = 0

    for y in range(sy + 1, rows):
        next_beams = defaultdict(int)

        for x, k in beams.items():
            if x < 0 or x>= cols:
                exited += k
                continue

            if lines[y][x] == "^":
                next_beams[x - 1] += k
                next_beams[x + 1] += k
            else:
                next_beams[x] += k

        beams = next_beams

        if beams and all(x < 0 or x >= cols for x in beams):
            exited += sum(beams.values())
            return exited

    exited += sum(beams.values())
    return exited

with open('inputs/day7.txt') as f:
    line = f.read().strip("\n")

print(count_splits(line))
print(count_timelines(line))