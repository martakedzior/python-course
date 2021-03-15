# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.


def range_check(range_input1, range_input2, number_to_check):
    if range_input2 >= number_to_check >= range_input1:
        print(f'Value {number_to_check} is within the range {range_input1} - {range_input2}.')
    else:
        print(f'Value {number_to_check} is outside of the range {range_input1} - {range_input2}.')


range_check(34, 78, 10)
range_check(4, 78, 10)
range_check(9.99, 78, 10)
range_check(10, 78, 10)
range_check(10.1, 78, 10)
