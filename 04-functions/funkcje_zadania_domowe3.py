#3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).


def maximum_of(a, b, c):
    if a > b and a > c:
        print(f'Minimal value out of three: {a}, {b}, {c} is {a}')
    elif b > a and b > c:
        print(f'Minimal value out of three: {a}, {b}, {c} is {b}')
    elif c > a and c > b:
        print(f'Minimal value out of three: {a}, {b}, {c} is {c}')


maximum_of(20, 2, 10)
maximum_of(1, 10, 11)
maximum_of(9, 11, 5)