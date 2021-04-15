user_input = input('Gimme a number: ')

try:
    result = 10 / float(user_input)
    print(result)
except ValueError as e:
    print('This is not a number')
    print(e)
except ZeroDivisionError as err:
    print("You can't divide by zero!")
    print('Temp result: ', 0)
    print(err)

