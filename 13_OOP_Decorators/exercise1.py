#  Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
#  Utwórz funkcję zwracającą tekst
#    Utwórz dekorator przyjujący tę funkcję
#    Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(func):
    def wrapper():
        # txt = func()
        # txt = txt.upper()
        # return txt
        return func().upper()
    return wrapper #sama nazwa bez wywolania, uzywanie jako dekorator

@uppercase_decorator
def lorem_generator():
    return 'lorem ipsum dolor sit amet'



print(lorem_generator())