# 2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of(a, b, c):
    if a < b and a < c:
        print(f'Minimal value out of three: {a}, {b}, {c} is {a}')
    elif b < a and b < c:
        print(f'Minimal value out of three: {a}, {b}, {c} is {b}')
    elif c < a and c < b:
        print(f'Minimal value out of three: {a}, {b}, {c} is {c}')


minimum_of(20, 2, 10)
minimum_of(1, 10, 11)
minimum_of(9, 11, 5)