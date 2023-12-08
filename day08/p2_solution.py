from math import lcm
import sys

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

path = lines[0].replace("R", "1").replace("L", "0")

lines = lines[2:]

inputs = []

nodes = {}
for line in lines:
    k = line.split("=")[0].strip()
    if k.endswith("A"):
        inputs.append(k)
    v = line.split("=")[1].strip().replace("(", "").replace(")", "").strip().split(",")
    v = [x.strip() for x in v]
    nodes[k] = (v[0], v[1])


def solve(input, path, nodes) -> int:
    i = 0
    steps = 0
    current = input
    while True:
        steps += 1
        current_turn = path[i]
        current = nodes[current][int(current_turn)]
        if current.endswith("Z"):
            return steps
        i = (i + 1) % len(path)


steps = []
for input in inputs:
    steps.append(solve(input, path, nodes))

print(lcm(*steps))
