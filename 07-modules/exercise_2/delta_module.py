
#
# Wzór na deltę
#
# Delta \Delta inaczej wyróżnik trójmianu kwadratowego.
#
# Mając funkcję kwadratową postaci:
#
# f(x) = ax^2 + bx + c
#
# gdzie: a, b, c są współczynnikami funkcji kwadratowej i a!= 0

# delta = b^2 - 4ac

def delta(a, b, c):
    delta_calculation = b ** 2 - 4 * a * c
    return delta_calculation

if __name__ == "__main__":
    print(delta(3, 7, -2))