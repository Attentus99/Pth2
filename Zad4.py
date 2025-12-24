total = 0

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            number = int(line)
            total += number

print(f"Suma liczb: {total}")
