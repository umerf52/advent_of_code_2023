import sys

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

times = map(int, lines[0].split(":")[1].strip().split())
distances = map(int, lines[1].split(":")[1].strip().split())

tuples = list(zip(times, distances))

result = 1

for t in tuples:
    possible_wins = 0
    for held in range(t[0] + 1):
        time_left = t[0] - held
        total = held * time_left
        if total > t[1]:
            possible_wins += 1
    result *= possible_wins

print(result)
