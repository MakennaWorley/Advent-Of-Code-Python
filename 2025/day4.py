# day 4
with open('inputs/day4.txt') as f:
    grid = [list(line.strip()) for line in f if line.strip()]

rows = len(grid)
cols = len(grid[0])

dir = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

accessible = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue

        neighbors = 0
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                neighbors += 1

        if neighbors < 4:
            accessible += 1

print(accessible)

total_remove = 0

while True:
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    neighbors += 1

            if neighbors < 4:
                to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = 'X'

    total_remove += len(to_remove)

print(total_remove)