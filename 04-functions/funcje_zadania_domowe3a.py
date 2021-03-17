#3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_2(arg_1, arg_2):
    return arg_1 if arg_1 > arg_2 else arg_2

def maximum_of(a, b, c):
    return max_of_2(c, max_of_2(a, b))

print(max_of_2(5, 7))

print(maximum_of(10, 4, 9))