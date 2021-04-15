# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

def test_tuple(sample_tuple):
    user_input = int(input(f'Podaj proszę indeks elementu, który mam wyświetlić od 0 do {len(sample_tuple) - 1} : '))
    print(f'Pod tym indeksem kryje się element: {sample_tuple[user_input]}')
    user_element = input('Podaj element jakim chcesz zastąpić tą wartość w krotce: ')
    sample_tuple[user_input] = user_element


if __name__ == "__main__":
    sample_tuple = ((1,2), ('rtrt', 89), 34.4, 'tekst', True, False, 0, ['d'])

    try:
        test_tuple(sample_tuple)
    except TypeError as err:
        print('Nie można podmienić elementu krotki. ', err)