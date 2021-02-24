# IF instrukcje warunkowe

dish = "gzik"

if dish == "gzik":
    print("Wielkopolska")
else:
    print("Nie wiem")

# niezdefiniowana zmienna

if dish == "pyzy":
    reg = "Wielkopolska"
print(reg)

# Operator trójargumentowy

feb = 29 if leap_year else 28

if leap_year:
    feb = 29
else:
    feb = 28
