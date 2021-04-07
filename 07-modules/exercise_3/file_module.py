# 3▹ Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz
# bezpieczny zapis. Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

def read_file(filename):
    text = '***'
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        return 'file not found error'

    if text == '':
        return 'file is empty'

    return text


def save_file(filename, content):
    try:
        with open(filename, 'x', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'

    return 'file successfully saved'