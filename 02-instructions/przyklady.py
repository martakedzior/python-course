# IF instrukcje warunkowe

dish = "gzik"

if dish == "gzik":
    print("Wielkopolska")
else:
    print("Nie wiem")

# niezdefiniowana zmienna

# if dish == "pyzy":
#     reg = "Wielkopolska"
# print(reg)

# Operator trójargumentowy

leap_year = True

feb = 29 if leap_year else 28

if leap_year:
    feb = 29
else:
    feb = 28

# opcjonalne klauzule:
season = 'wiosna'

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')