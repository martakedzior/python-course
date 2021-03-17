# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

secret_number = 5
previous_guess = - 100

while True:
    user_number = int(input('Give me your guess: '))
    if user_number == secret_number:
        break

    if abs(secret_number - user_number) < abs(previous_guess):
        print('warm!')
        previous_guess = abs(secret_number - user_number)
    else:
        print('cold!')


print('Congratulations - you win!')
