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

    hex_code = splitted[2]
    value = hex_code[2:7]

    decimal_value = int(value, 16)
    direction = splitted[2][-2]

    if direction == "0":
        x += int(decimal_value)
        perimeter += int(decimal_value)
    elif direction == "2":
        x -= int(decimal_value)
        perimeter += int(decimal_value)
    elif direction == "3":
        y -= int(decimal_value)
        perimeter += int(decimal_value)
    elif direction == "1":
        y += int(decimal_value)
        perimeter += int(decimal_value)

    coords.append((x, y))

numpy_x = np.array([x[0] for x in coords])
numpy_y = np.array([x[1] for x in coords])

area = shoelace(numpy_x, numpy_y)

print(int(area + (perimeter // 2) + 1))
