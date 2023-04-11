lines = []

with open("vykaz.txt", encoding="utf-8") as file:
    for line in file:
        print(int(line) * 120)