#obsługa błędu w przypadku jeśli plik nie istnieje
filename = 'text.txt'

with open(filename, 'r', encoding='utf-8') as file:
    content = file.readlines()

print("---------------------")

for index in range(len(content)):
    print(f"{index}  -> {content[index]}")

# można użyć enumerate()
for index, line in enumerate(content):
    print(index, '-->', line)