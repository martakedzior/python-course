# 7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
#     American Express card numbers start with 34 or 37 and have 15 digits.


def user_input():
    user_entered_card_nr = input('Please enter card number: ')
    user_entered_card_nr = user_entered_card_nr.replace(' ', '')

    while user_entered_card_nr.isdigit() is not True:
        user_entered_card_nr = input('Please enter card number - use digits only: ').replace(' ', '')

    if len(user_entered_card_nr) not in [13, 15, 16]:
        print('It is not a card number.')

    return user_entered_card_nr


def check_if_Visa(user_entered_card_nr):
    if user_entered_card_nr[0] == '4' and len(user_entered_card_nr) in [13, 16]:
        return True
    else:
        return False


def check_if_MasterCard(user_entered_card_nr):
    if len(user_entered_card_nr) == 16 and (51 <= int(user_entered_card_nr[0:2]) <= 55 or 2221 <= int(user_entered_card_nr[0:4]) <= 2720):
        return True
    else:
        return False


def check_if_American_Express(user_entered_card_nr):
    if len(user_entered_card_nr) == 15 and user_entered_card_nr[0:2] in ['34', '37']:
        return True
    else:
        return False

def card_check():
    card_number = user_input()

    if check_if_Visa(card_number):
        print('This is Visa Card!')
    elif check_if_MasterCard(card_number):
        print('This is Master Card! ')
    elif check_if_American_Express(card_number):
        print('This is American Express! ')
    else:
        print('This is some other credit card! ')


card_check()


