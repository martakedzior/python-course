# xmas.py

def print_triangle(n):
    for size in range(1, n+1, 2):
        print(size * "*")

for i in range(2, 5):
    print_triangle(i)