# Napiszać funkcję, która oblicza pole koła na podstawie zadanego promienia
# Pi * r *2

import math

def circle_array(radius):
    return math.pi * radius ** 2

print(f'Pole koła o podanym promieniu wynosi {circle_array(4)}')