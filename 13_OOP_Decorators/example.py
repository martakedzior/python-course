def hello():
    name = 'Ala'

    def good_morning(counter):  #funkcja lokalna (prywatna dla hello)
        return name * counter

    return good_morning

# domknięcie

welcome_fun = hello()

print(welcome_fun(4))