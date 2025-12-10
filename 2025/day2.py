# day 2
def is_invalid(n: int):
    s = str(n)

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]

def is_invalid2(n: int):
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue

        chunk = s[:k]
        repetitions = L // k

        if chunk * repetitions == s and repetitions >= 2:
            return True

    return False

total = 0
total2 = 0

with open('inputs/day2.txt') as f:
    line = f.read().strip()
    ranges = line.split(",")

    for r in ranges:
        start, end = r.split("-")

        #print(start, end)

        for n in range(int(start), int(end) + 1):
            if is_invalid(n):
                total += n
            if is_invalid2(n):
                total2 += n

print(total)
print(total2)