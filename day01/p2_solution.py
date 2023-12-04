digits_dict = {
    "one": "on1e",
    "two": "tw2o",
    "three": "th3ee",
    "four": "fo4r",
    "five": "fi5e",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "ni9e",
}

total = 0

with open("input_file.txt") as f:
    for line in f:
        line = line.strip()

        for key in digits_dict.keys():
            line = line.replace(key, digits_dict[key])

        digits = "".join(list(filter(lambda x: x.isdigit(), line)))

        if len(digits) < 2:
            digits = digits + digits
        else:
            digits = digits[0] + digits[-1]

        total += int(digits)

print(total)
