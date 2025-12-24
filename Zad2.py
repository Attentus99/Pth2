with open("story.txt", "r", encoding="utf-8") as file:
    word_count = 0

    for line in file:
        line = line.strip()        # usuń białe znaki
        if line:                   # ignoruj puste linie
            words = line.split()   # podziel linię na słowa
            word_count += len(words)

print(f"Liczba słów: {word_count}")
