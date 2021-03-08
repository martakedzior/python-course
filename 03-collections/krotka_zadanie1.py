#1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.

pet_data = ('kot', 'ragdoll', 'Aramis')

(animal, breed, name) = pet_data

print(f'Mój {animal}, rasy {breed} wabi się {name}')

