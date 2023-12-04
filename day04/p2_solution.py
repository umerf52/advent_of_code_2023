from collections import defaultdict
import sys

total = 0

file_name = sys.argv[1]

with open(file_name) as f:
    card_i = 1
    cards = defaultdict(int)
    for line in f:
        cards[card_i] += 1
        line = line.strip().split(":")[1].strip()
        winning, drawn = line.split("|")[0], line.split("|")[1]
        winning, drawn = winning.split(), drawn.split()
        winning, drawn = {int(x) for x in winning}, {int(x) for x in drawn}
        matches = winning.intersection(drawn)

        multiply_factor = cards[card_i]
        for i in range(len(matches)):
            cards[card_i + i + 1] += 1 * multiply_factor

        card_i += 1

print(sum(cards.values()))
