REDS = 12
GREENS = 13
BLUES = 14

total = 0

with open("input_file.txt") as f:
    game_id = 1
    for line in f:
        is_valid = True
        line = line.split(":")[1]
        line = line.replace(";", ",")
        draws = line.split(", ")
        draws = [draw.strip() for draw in draws]
        for draw in draws:
            count, color = int(draw.split(" ")[0]), draw.split(" ")[1]
            count = int(count)
            if color == "red" and count > REDS:
                is_valid = False
                break
            elif color == "green" and count > GREENS:
                is_valid = False
                break
            elif color == "blue" and count > BLUES:
                is_valid = False
                break

        if is_valid:
            total += game_id
        game_id += 1

print(total)
