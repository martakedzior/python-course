# 5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

#Przykład palindromu:
palindrom = "Kobyła ma mały bok"
if_palindrom = palindrom.lower().replace(" ","")

if if_palindrom == if_palindrom[::-1]:
    print(f'Phrase: "{palindrom}" is palindrom.')
else:
    print(f'Phrase: "{palindrom}" is not palindrom.')

# User input
user_input = input('Please provide a phrase and I will check if it is palindrom: ')

if user_input.lower().replace(" ","").replace(".","") == user_input.lower().replace(" ","").replace(".","")[::-1]:
    print(f'Phrase: "{user_input}" is palindrom.')
else:
    print(f'Phrase: "{user_input}" is not palindrom.')

