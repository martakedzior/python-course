# 5▹ Stwórz moduł obliczający pola różnych figur. W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów
# pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku.

from shapes_library import triangle_area, rectangle_aera, trapezium_area


if __name__ == '__main__':
    flat = [
        ['rectangle', 4, 3.2],
        ['trapezoid', 4, 3, 3],
        ['rectangle', 3, 3],
        ['triangle', 3, 4]
    ]

    area_of_flat = 0

    for room in flat:
        if room[0] == 'rectangle':
            area_of_flat = rectangle_aera(room[1], room[2]) + area_of_flat
        if room[0] == 'triangle':
            area_of_flat = triangle_area(room[1], room[2]) + area_of_flat
        if room[0] == 'trapezoid':
            area_of_flat = trapezium_area(room[1], room[2], room[3]) + area_of_flat

    print(f'Flat area is: {area_of_flat}')