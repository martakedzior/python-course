# 3▹ Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz
# bezpieczny zapis. Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import file_module as fm

if __name__ == '__main__':
    print(fm.read_file('test.txt'))

    text_to_save = 'Lalalalal'
    print(fm.save_file('save.txt', text_to_save))