# 1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

def division(elements):
    for element in elements:
        try:
            result = 10 / element

        except ZeroDivisionError as err:
            print("Don't divide by zero! ", err)

        except TypeError as err:
            print("This is not a number! ", err)

    return result


if __name__ == "__main__":
    elements = [13, 'tekst', 2.45, 0, 'Af3']
    result = division(elements)
    print(result)
