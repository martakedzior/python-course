#obsługa błędu w przypadku jeśli plik nie istnieje
filename2 = 'plik.txt'
try:
    with open(filename2, 'r', encoding='utf-8') as file:
        content = file.readlines()
        print(content)
except FileNotFoundError:
    print('Błąd otwarcia pliku. ')

for l in range(len(content)):
    print("line " + str(l) + ":", content[l])