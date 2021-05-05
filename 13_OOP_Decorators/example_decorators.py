def say_hello_decorator(func_param):

    def good_morning():  #funkcja lokalna (prywatna dla hello)
        print('Good morning')
        func_param()

    return good_morning

def small_talk():
    print('How are you today?')


meeting = say_hello_decorator(small_talk) # good morning

meeting()