import sys
from itertools import groupby

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

seeds = lines[0].split(": ")[1].split()
seeds = [int(seed) for seed in seeds]
lines = lines[1:]

groups = [list(g) for k, g in groupby(lines, key=bool) if k]

locations = []
for result in seeds:
    # seed to soil
    for line in groups[0][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # soil to fertilizer
    for line in groups[1][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # fertilizer to water
    for line in groups[2][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # water to light
    for line in groups[3][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # light to temperature
    for line in groups[4][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # temperature to humidity
    for line in groups[5][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    # humidity to location
    for line in groups[6][1:]:
        data = line.split()
        dest, src, offset = int(data[0]), int(data[1]), int(data[2])
        r = range(src, src + offset)
        if result in r:
            result = abs(result - src) + dest
            break

    locations.append(result)

print(min(locations))
