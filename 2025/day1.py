# day 1
i = 50

password = 0
pass0 = 0

with open('inputs/day1.txt') as f:
    for line in f:
        line = line.strip()
        steps = int(line[1:])

        if line[0] == 'L':
            if i == 0:
                first = 100
            else:
                first = i

            if first <= steps:
                pass0 += 1 + (steps - first) // 100

            i = (i - steps) % 100


        if line[0] == 'R':
            if i == 0:
                first = 100
            else:
                first = 100 - i

            if first <= steps:
                pass0 += 1 + (steps - first) // 100

            i = (i + steps) % 100
        #print(line, numbers[i])

        if i == 0:
            password+=1

print(password)
print(pass0)