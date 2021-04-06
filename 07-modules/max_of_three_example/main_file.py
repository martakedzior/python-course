import max_of_three as m3

def get_three_values():
    v1 = int(input('Podaj 1. liczbę całkowitą: '))
    v2 = int(input('Podaj 2. liczbę całkowitą: '))
    v3 = int(input('Podaj 3. liczbę całkowitą: '))
    return v1, v2, v3

def main():
    a, b, c = get_three_values()
    print(m3.maximum_of(a, b, c))

if __name__ == "__main__":
    main()
