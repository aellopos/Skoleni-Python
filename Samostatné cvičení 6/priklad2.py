lines = []
celkovy_pocet = 0

with open('slohovka.txt', encoding='utf-8') as file:
    for line in file:
        lines.append(line.split())

print(lines)

for r in lines:
    print(f"{len(r)}")
    celkovy_pocet += len(r)

print(celkovy_pocet)