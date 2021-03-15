# Stwórz plik bmi.py i napisz program, który obliczy BMI:
# BMI = (masa (kg)) / (wzrost (m))²

weight = 64
height = 1.68

BMI = weight / height ** 2
BMI_rounded = round(BMI, 2)
print("Your BMI is:", BMI)
