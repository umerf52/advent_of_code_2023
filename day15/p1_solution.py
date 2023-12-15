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


total = 0
for s in data:
    total += hash_func(s)

print(total)
