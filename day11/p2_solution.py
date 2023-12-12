import sys
import numpy as np

file_name = sys.argv[1]

f = open(file_name, "r")
data = f.read().splitlines()
f.close()

data = np.array([list(line) for line in data])


def get_empty(lines) -> ([int], [int]):
    rows = []
    for i in range(len(lines)):
        dots = np.count_nonzero(lines[i] == ".")
        if dots == len(lines[0]):
            rows.append(i)

    cols = []
    lines = lines.transpose()
    for i in range(len(lines)):
        dots = np.count_nonzero(lines[i] == ".")
        if dots == len(lines[0]):
            cols.append(i)

    return rows, cols


empty_rows, empty_cols = get_empty(data.copy())

galaxies = []

# find galaxies
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            galaxies.append((i, j))

# make unique pairs
pairs = []
for i, galaxy in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        pairs.append((galaxy, galaxies[j]))

# find distance between each pair
distance = 0
for pair in pairs:
    temp_dist = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    x_range = sorted([pair[0][0], pair[1][0]])
    y_range = sorted([pair[0][1], pair[1][1]])
    x_traversed = 0
    for row in empty_rows:
        if row in range(x_range[0], x_range[1]):
            x_traversed += 1

    y_traversed = 0
    for col in empty_cols:
        if col in range(y_range[0], y_range[1]):
            y_traversed += 1

    distance += temp_dist + ((x_traversed + y_traversed) * (1_000_000 - 1))

print(distance)
