# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
# BMI = (masa (kg)) / (wzrost (m))²

def bmi_calculation(weight, height_m):
    bmi = weight / (height_m ** 2)
    bmi_rounded = round(bmi, 2)
    print('Moje BMI =', bmi_rounded)

    return bmi_rounded


def bmi_evaluation(bmi_rounded):

    if bmi_rounded <= 18:
        print('To jest niedowaga!')
        return "underweight"
    elif 24.99 > bmi_rounded > 18:
        print('To jest waga normalna')
        return "normal"
    elif 29.99 > bmi_rounded > 24.99:
        print('To jest nadwaga')
        return "overweight"
    else:
        print('To jest otyłość')
        return "obesity"


if __name__ == ('__main__'):
    bmi_rounded = bmi_calculation()
    bmi_evaluation(bmi_rounded)
    evaluation=bmi_evaluation(bmi_rounded)

