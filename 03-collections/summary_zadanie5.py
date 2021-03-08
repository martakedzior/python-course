# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

# Zadbaj o sposób wyświetlania np.:
#
#     szybko : 5
#
#     zbudź : 1

poem = poem.lower()
poem = poem.replace(',', '')
poem = poem.split()

poem_dict = {}
for word in poem:
    if word in poem_dict:
        poem_dict[word] = poem_dict[word] + 1
    else:
        poem_dict[word] = 1

for key, value in poem_dict.items():
    print(key, ':', value)
