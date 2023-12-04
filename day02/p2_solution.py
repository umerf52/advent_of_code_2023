total = 0

with open("input_file.txt") as f:
    for line in f:
        max_counts = {"red": 0, "green": 0, "blue": 0}
        line = line.split(":")[1]
        line = line.replace(";", ",")
        draws = line.split(", ")
        draws = [draw.strip() for draw in draws]

        for draw in draws:
            count, color = int(draw.split(" ")[0]), draw.split(" ")[1]
            max_counts[color] = max(max_counts[color], count)

        total = total + max_counts["red"] * max_counts["green"] * max_counts["blue"]

print(total)
