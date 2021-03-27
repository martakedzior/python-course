# 7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
#     American Express card numbers start with 34 or 37 and have 15 digits.


def card_input():
    # czytanie z pliku
    filename = 'credit_cards.txt'

    with open(filename, 'r', encoding='utf-8') as cards:
        user_entered_cards = cards.readlines()

    return user_entered_cards


def check_if_credit_card(user_entered_card_nr):
    if len(user_entered_card_nr) not in [13, 15, 16]:
        return False
    else:
        return True


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


def save_cards_number(filename, card_number):
    with open(filename, "a") as fp:
        fp.write(card_number + '\n')


# main code
card_number = card_input()

for card in card_number:
    card = card.replace(" ","").replace("\n","").strip()

    if check_if_credit_card(card):
        if check_if_Visa(card):
            print('This is Visa Card!')
            save_cards_number('visa.txt', card)
        elif check_if_MasterCard(card):
            print('This is Master Card! ')
            save_cards_number('mastercard.txt', card)
        elif check_if_American_Express(card):
            print('This is American Express! ')
            save_cards_number('americanexpress.txt', card)
        else:
            print('This is some other credit card! ')
            save_cards_number('other.txt', card)
    else:
        print('It is not a valid card number.')

