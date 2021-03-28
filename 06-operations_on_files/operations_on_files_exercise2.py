# 2▹ Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os
import time

quotes_file = "C:/Users/Marta/Desktop/cytaty.txt"

# Pozyskiwanie bieżącej ścieżki dostępu za pomocą funkcji os.getcwd:
print(os.getcwd())

# Zmiana ścieżki dostępu za pomocą funkcji os.chdir:
os.chdir("C:/Users/Marta/Desktop/")
print(os.getcwd())

# Uzyskanie listy plików i folderów zawartych w danej lokalizacji za pomocą funkcji os.listdir:
l = list(os.listdir())
print(l)

# Pozyskanie rozmiaru pliku w bajtach za pomocą funkcji os.path.getsize:
print(f'Rozmiar pliku {quotes_file} wynosi {os.path.getsize("C:/Users/Marta/Desktop/cytaty.txt")} bajtów')

# Pozyskanie daty utworzenia pliku za pomocą funkcji os.path.getctime:
print(time.ctime(os.path.getctime(quotes_file)))

# Usuwanie pliku za pomocą funkcji os.remove:
with open("plik.txt", "w", encoding='utf-8') as fp:
    fp.write("jakiś tam tekst")

os.remove("plik.txt")

