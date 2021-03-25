# zapis do pliku z listy musi użyć metody join żeby zamienić elementy z listy na stringi

sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']

with open('save1.txt', 'w') as f:
    f.write('\n'.join(sweets_list))