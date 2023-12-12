import sys
import numpy as np

file_name = sys.argv[1]

f = open(file_name, "r")
data = f.read().splitlines()
f.close()

data = np.array([list(line) for line in data])


def expand_rows(lines) -> np.array:
    indices = []
    for i in range(len(lines)):
        dots = np.count_nonzero(lines[i] == ".")
        if dots == len(lines[0]):
            indices.append(i)

    # insert rows at indices
    while len(indices) > 0:
        i = indices.pop(0)
        lines = np.insert(lines, i, np.full((1, lines.shape[1]), "."), axis=0)
        indices = [x + 1 for x in indices]

    return lines


# expand rows
data = expand_rows(data)
# expand columns
data = expand_rows(data.transpose())

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
    distance += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

print(distance)
