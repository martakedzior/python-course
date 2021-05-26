def clousure():
    a = "closure" #obiekt string

    def nested(b):
        return a * b #instrukcja wykorzystujaca obiekt z zakresu

    return nested

new_function = clousure()

print(new_function(4))