# otwiera plik i potrzebne jest zamknięcie pliku
f = open('plik.txt')  # otwórz do odczytu
print(f.readline())
f.close()

# metoda with otwiera i od razu zamyka
with open('plik.txt') as f:
    print(f.readline())

#czytanie z pliku Inwokacji Pana Tadeusza
filename = 'text.txt'

with open(filename, 'r', encoding='utf-8') as inwokacja:
    content = inwokacja.read()
    print(content)

with open(filename, 'r') as file:
    content = file.readlines()
    print(content)

with open(filename, 'r') as file:
    content = file.readline()
    print(content)

#obsługa błędu w przypadku jeśli plik nie istnieje
filename2 = 'text2.txt'
try:
    with open(filename2, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Błąd otwarcia pliku. ')

#odczyt po linii - dobra praktyka trzeba uzywac readlines() zamiast jakiegos for czy while (zła praktyka)
with open('plik.txt', 'r') as fopen:
  lines = fopen.readlines()

for l in range(len(lines)):
  print("Line " + str(l), lines[l])