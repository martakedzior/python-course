# 3▹ Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz
# bezpieczny zapis. Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

def open_file(filename):
    text = "***"
    try:
        with open(filename) as file:
            text = file.read()
    except FileExistsError:
        print('File exist error.')
        
    except FileNotFoundError:
        print('File not found.')

    return text

