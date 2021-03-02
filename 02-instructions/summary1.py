#1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

names = "Ruby, Ada, Julia, Anna" #input

names = names.replace(' ','').split(',')

print(names)

for name in names:
    print(f'Hello {name}!')