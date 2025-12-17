# day 5
with open('inputs/day5.txt') as f:
    lines = [line.strip() for line in f]

ranges = []
ids = []

i = 0
while i < len(lines) and lines[i] != "":
    a, b = map(int, lines[i].split("-"))
    ranges.append((a, b))
    i += 1

while i < len(lines) and lines[i] == "":
    i += 1

while i < len(lines):
    ids.append(int(lines[i]))
    i += 1

fresh = 0
for x in ids:
    if any(a <= x <= b for a, b in ranges):
        fresh += 1

print(fresh)

ranges.sort()

merged = []
for a, b in ranges:
    if not merged:
        merged.append([a, b])
        continue

    prev_a, prev_b = merged[-1]
    if a <= prev_b + 1:
        merged[-1][1] = max(prev_b, b)
    else:
        merged.append([a, b])

print(sum(b-a+1 for a, b in merged))