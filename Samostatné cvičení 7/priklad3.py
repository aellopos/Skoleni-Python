vykaz = [10, 101, 123, 42, 34, 67, 456, 45, 54, 43, 12, 32]
mesic = 1

with open("vykaz.txt", mode="a", encoding="utf-8") as file: 
    for cas in vykaz:
        print(f"{mesic} - {cas * 100}", file=file)
        mesic += 1