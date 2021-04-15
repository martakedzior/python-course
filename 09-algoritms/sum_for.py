def sum_naturals(n):
    sum_number = 0

    for nr in range(1, n+1):
        sum_number = sum_number + nr

    return sum_number


def sum_naturals_while(n):
    sum_number = 0

    while n > 0:
        sum_number += n
        n = n - 1

    return sum_number


def sum_naturals_recursion(n):
    # 10 + sum_naturals_recursion(9)
    #     9 + sum_naturals_recursion(8)
    #         8 + sum_naturals_recursion(7)
    #             ...
    #             2 + sum_naturals_recursion(1)
    #                 n

    if n == 1:
        return 1
    else:
        return n + sum_naturals_recursion(n-1)


print(sum_naturals(10))

print(sum_naturals_while(10))

print(sum_naturals_recursion(10))