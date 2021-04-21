# 4▹ Oblicz średnią arytmetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią. Program powinien być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.


def user_input():
    user_input = ""
    user_input = input('Podaj liczby z których chcesz wyliczyć średnią arytmetyczną po przecinku: ')
    user_input = user_input.replace(' ', '').split(',')

    return user_input


def input_validation(user_input):
    number_list = []

    for item in user_input:
        try:
            item = int(item)
            number_list.append(item)
        except (ValueError, TypeError):
            item = 0
            number_list.append(item)

    return number_list


def calculate_average(number_list):
    user_input_avg = sum(number_list) / len(number_list)
    return user_input_avg


if __name__ == "__main__":
    number_list = input_validation(user_input())
    user_input_avg = calculate_average(number_list)
    print(f"Średnia z podanych liczb {number_list} to: {user_input_avg}")