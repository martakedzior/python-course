# BMI = (masa (kg)) / (wzrost (m))²
waga = int( input('Podaj swoją wagę [kg]:') )
wzrost_cm = int(input('Podaj swój wzrost [cm]:'))
wzrost_m = wzrost_cm / 100
BMI = waga / (wzrost_m ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI =', BMI_rounded)