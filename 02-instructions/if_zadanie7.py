# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
# BMI = (masa (kg)) / (wzrost (m))²

weight = int(input('Podaj swoją wagę [kg]:'))
height_cm = int(input('Podaj swój wzrost [cm]:'))
height_m = height_cm / 100
BMI = weight / (height_m ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI =', BMI_rounded)

if BMI_rounded <= 18:
    print('To jest niedowaga!')
elif 24.99 > BMI_rounded > 18:
    print('To jest waga normalna')
elif 29.99 > BMI_rounded > 24.99:
    print('To jest nadwaga')
else:
    print('To jest otyłość')


