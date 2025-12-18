# day 6
from math import prod

with open("inputs/day6.txt", "r") as f:
    raw = [line.rstrip("\n") for line in f]

lines = [ln for ln in raw if ln.strip() != ""]

cols = max(len(ln) for ln in lines)
grid = [ln.ljust(cols) for ln in lines]
rows = len(grid)

signs = [all(grid[r][c] == " " for r in range(rows)) for c in range(cols)]

slices = []
c = 0
while c < cols:
    while c < cols and signs[c]:
        c += 1
    if c >= cols:
        break
    L = c
    while c < cols and not signs[c]:
        c += 1
    R = c - 1
    slices.append((L, R))

total1 = 0

for L, R in slices:
    nums = []
    op = None

    for r in range(rows):
        chunk = grid[r][L:R+1]
        s = chunk.strip()
        if not s:
            continue

        if "+" in s:
            op = "+"
            continue
        if "*" in s:
            op = "*"
            continue

        nums.append(int(s))

    total1 += sum(nums) if op == "+" else prod(nums)

print(total1)

total2 = 0

for L, R in slices:
    op = None

    for c in range(L, R+1):
        if grid[rows-1][c] in "*+":
            op = grid[rows-1][c]
            break

    nums = []

    for c in range(R, L-1, -1):
        digits = []
        for r in range(rows-1):
            chunk = grid[r][c]
            if chunk.isdigit():
                digits.append(int(chunk))

        if digits:
            nums.append(int("".join(map(str, digits))))

    total2 += sum(nums) if op == "+" else prod(nums)

print(total2)