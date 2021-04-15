def check(result):
    try:
        x = 1/result[int(input('Podaj nr indeksu:'))]
        print(x)
        print('Jest ok!')
    except ValueError as e:
        print('This is not a number')
        print(e)
    except ZeroDivisionError as e:
        print("You can't divide by 0")
        print('Temp result:', 0)
        print(e)
    except SyntaxError as e:
        print('To jest string')
        print(e)
    except TypeError as e:
        print('No correct input format')
        print(e)


somthing = (1, 0, 'a', [10], {2},{'x':2}, 2.5)

check(somthing)