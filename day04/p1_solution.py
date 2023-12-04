import sys

total = 0

file_name = sys.argv[1]

with open(file_name) as f:
    for line in f:
        line = line.strip().split(":")[1].strip()
        winning, drawn = line.split("|")[0], line.split("|")[1]
        winning, drawn = winning.split(), drawn.split()
        winning, drawn = {int(x) for x in winning}, {int(x) for x in drawn}
        matches = winning.intersection(drawn)
        if len(matches) > 0:
            total += 2 ** (len(matches) - 1)

print(total)
