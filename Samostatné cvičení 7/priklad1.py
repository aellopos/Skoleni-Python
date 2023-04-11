pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("kalendar.txt", mode='w', encoding='utf-8') as output_file: 
	for dny in pocty_dni: 
	    print(dny, file=output_file)
