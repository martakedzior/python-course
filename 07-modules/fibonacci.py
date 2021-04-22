#7▹ Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.

def Fibonacci(n):
    fibonacci = [0]
    calculate = 0
    for i in range(0, n):
        if i == 0 or i == 1:
            fibonacci.append(1)
        else:
            calculate = fibonacci[i] + fibonacci[i-1]
            fibonacci.append(calculate)

    print(fibonacci)