name = input("Zadej jmeno souboru: ")
line = input("Zadej radek souboru: ")

with open(name, mode="w", encoding="utf-8") as file: 
    print(line, file=file)