#Praca z dokumentacją
#1. Jak sprawdzić czy ciąg znaków składa się tylko z cyfr?
#2. Jak wyświetlić wyśrodkowany tekst o zadanej szerokości i dodatkowo puste miejsca wypełnić np. gwiazdką: '***mata***'
#3. Jaka metoda usunie znaki tylko z prawej strony?
#4. Jak sprawdzić czy ciąg ma co najmniej jedną dużą literę?
#5. Policzy ile razy zadany ciąg znaków np. ('na') wystapił w ciągu znaków ('banana' =2)

# 1. metoda isdigit()
txt1 = "4323535"
txt2 = "a3dgg3"

print(txt1.isdigit())
print(txt2.isdigit())

# 2.
txt3 = 'mata'
print(txt3.center(10,'*'))

# 3.
txt4 = '***mata***'
print(txt4.rstrip('*'))

# 4.
txt5 = 'baNana'
print(txt5.isupper())

# 5.
txt6 = 'Banana'
print(txt6.count('na'))