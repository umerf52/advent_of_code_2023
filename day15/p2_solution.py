import sys

file_name = sys.argv[1]

f = open(file_name, "r")
data = f.read().splitlines()
f.close()

data = data[0].split(",")


def hash_func(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current = current % 256
    return current


hash_map = [None] * 256
for s in data:
    if "=" in s:
        key, value = s.split("=")
        index = hash_func(key)
        if hash_map[index] is None:
            hash_map[index] = {key: value}
        else:
            hash_map[index] = hash_map[index] | {key: value}
    else:
        key = s.split("-")[0]
        index = hash_func(key)
        if hash_map[index]:
            hash_map[index].pop(key, None)

total = 0
for i, v in enumerate(hash_map):
    if v:
        items = list(v.items())
        for item_i, item_v in enumerate(items):
            total += (i + 1) * (item_i + 1) * int(item_v[1])

print(total)
