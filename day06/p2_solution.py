import sys

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

possible_wins = 0

for held in range(time + 1):
    time_left = time - held
    total = held * time_left
    if total > distance:
        possible_wins += 1

print(possible_wins)
