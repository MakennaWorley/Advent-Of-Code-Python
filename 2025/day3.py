# day 3
def best_joltage(line: str):
    digits = line.strip()
    remove = len(digits) - 12
    stack = []

    for d in digits:
        while remove > 0 and stack and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    result_digits = ''.join(stack[:12])
    return int(result_digits)

volts1 = 0
volts2 = 0

with open('inputs/day3.txt') as f:
    for line in f:
        line = line.strip()

        max = 0

        for i in range(0, len(line)):
            for j in range(i + 1, len(line)):
                value = int(line[i] + line[j])

                if value > max:
                    max = value
                    #print(max)

        volts1 += max
        volts2 += best_joltage(line)

print(volts1)
print(volts2)