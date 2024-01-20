import sys
import numpy as np


def shoelace(_x, _y):
    return 0.5 * np.abs(np.dot(_x, np.roll(_y, 1)) - np.dot(_y, np.roll(_x, 1)))


file_name = sys.argv[1]

f = open(file_name, "r")
data = f.read().splitlines()
f.close()

perimeter, x, y = 0, 0, 0

coords = []
for line in data:
    splitted = line.split(" ")
    if splitted[0] == "R":
        x += int(splitted[1])
        perimeter += int(splitted[1])
    elif splitted[0] == "L":
        x -= int(splitted[1])
        perimeter += int(splitted[1])
    elif splitted[0] == "U":
        y -= int(splitted[1])
        perimeter += int(splitted[1])
    elif splitted[0] == "D":
        y += int(splitted[1])
        perimeter += int(splitted[1])

    coords.append((x, y))

numpy_x = np.array([x[0] for x in coords])
numpy_y = np.array([x[1] for x in coords])

area = shoelace(numpy_x, numpy_y)

print(int(area + (perimeter // 2) + 1))
