import sys

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

lines = [line.strip() for line in lines]
lines = [line.split() for line in lines]
lines = [[int(x) for x in line] for line in lines]

total = 0

for line in lines:
    pyramid = [line]
    while True:
        line = [t - s for s, t in zip(line, line[1:])]
        pyramid.append(line)
        if sum(line) == 0:
            break

    pyramid = pyramid[::-1]
    for i, v in enumerate(pyramid):
        if i > 0:
            pyramid[i].append(pyramid[i][-1] + pyramid[i - 1][-1])

    total += pyramid[-1][-1]

print(total)
