# Poniżej mamy listą zawierającą krotki. Wyświetl kalendarz dla każdego miesiąca:

def print_calendar(data):
    for month in data:
        print(month[0])
        print(" ")

        for i in month[1]:
            counter = i + 1
            dzien = str(counter).strip()

            if counter < 10:
                dzien = "0" + dzien

            print(dzien, end=" ")
            if (counter) % 7 == 0:
                print(" ")

        print(" ")
        print(" ")


# main program

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

print_calendar(data)
