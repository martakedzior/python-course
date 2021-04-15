# 1▹ Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
#
#     Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
#
#     Utwórz 4 pliki .txt zawierające porady.
#     Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
#     fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
#     Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.
#5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

from bmi_module import bmi_calculation, bmi_evaluation

def open_advice(filename):
    with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
        advice = file.read()
    return advice


def get_weight():
    while True:
        try:
            weight = int(input('Podaj wage w kg: '))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość')
            continue

        if weight > 35:
            break
        else:
            print('Twoja waga jest nieprawdopodobnie niska. Podaj wagę jeszcze raz.')

    return weight


def get_height():
    while True:
        try:
            height = float(input('Podaj wzrost w metrach: '))
        except (ValueError, TypeError):
            print('To nie jest prawidłowa wartość! Spróbuj jeszcze raz!')
            continue

        if 100 > height > 1.5:
            break
        else:
            print('Twoj wzrost jest podany nieprawidłowo. Podaj jeszcze raz!')

    return height


if __name__ == "__main__":
    m = get_weight()
    h = get_height()

    bmi_rounded = bmi_calculation(m, h)
    result = bmi_evaluation(bmi_rounded)
    print(open_advice(result))