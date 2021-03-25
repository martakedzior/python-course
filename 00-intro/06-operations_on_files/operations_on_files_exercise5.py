# 5▹ Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie.


def read_file():
    # czytanie z pliku Inwokacji Pana Tadeusza
    filename = 'save.txt'

    with open(filename, 'r', encoding='utf-8') as inwokacja:
        content = inwokacja.read()

    return content


def cleaning_text(text):
    # text = text.replace("!", " ").replace(".", "").replace(",", "")
    for i in ["!", ".", ","]:
        text = text.replace(i, "")

    clean_text = text.split()

    return clean_text


def looking_for_longest_word(text):
    longest = " "

    for word in text:
        if len(word) > len(longest):
            longest = word

    print(longest)


text = read_file()
clean_text = cleaning_text(text)
looking_for_longest_word(clean_text)




