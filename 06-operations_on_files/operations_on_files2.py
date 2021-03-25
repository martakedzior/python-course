#jak to wygląda jak uzywamy komendę open i coś się wywali przy / po otwieraniu
    
fopen = open('plik.txt', 'r')
print("I'm open")
print(fopen)
raise Exception("I'm rebel!")
fopen.close() # nie wykona się


