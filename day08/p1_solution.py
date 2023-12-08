import sys

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

path = lines[0].replace("R", "1").replace("L", "0")

lines = lines[2:]

nodes = {}
for line in lines:
    k = line.split("=")[0].strip()
    v = line.split("=")[1].strip().replace("(", "").replace(")", "").strip().split(",")
    v = [x.strip() for x in v]
    nodes[k] = (v[0], v[1])


i = 0
steps = 0
current = "AAA"
while True:
    steps += 1
    current_turn = path[i]
    current = nodes[current][int(current_turn)]
    if current == "ZZZ":
        break
    i = (i + 1) % len(path)

print(steps)
