def divide_by(number):
    number = float(number)
    return  10 / number


if __name__ == '__main__':
    user_input = input('Gimme a number: ')

    try:
        result = divide_by(user_input)
        print(result)
    except ValueError as e:
        print('This is not a number')
        print(e)
    except ZeroDivisionError as err:
        print("You can't divide by zero!")
        print('Temp result: ', 0)
        print(err)
    finally:
        print("Finally here!")