total = 0

with open('input_file.txt') as f:
    for line in f:
        line = line.strip()
        digits = ''.join(list(filter(lambda x: x.isdigit(), line)))
        if len(digits) < 2:
            digits = digits + digits
        else:
            digits = digits[0] + digits[-1]
        
        total += int(digits)

print(total)