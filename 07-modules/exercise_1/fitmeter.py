# 1▹ Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
#
#     Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
#
#     Utwórz 4 pliki .txt zawierające porady.
#
#     Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
#
#     fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
#
#     Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.

from bmi_module import bmi_calculation, bmi_evaluation

def open_advice(filename):
    with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
        advice = file.read()
    return advice


if __name__ == "__main__":
    bmi_rounded = bmi_calculation()
    result = bmi_evaluation(bmi_rounded)
    print(open_advice(result))