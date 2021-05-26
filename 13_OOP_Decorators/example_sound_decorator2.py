def sound_decorator(func_as_param):
    def hau_nested():
        print('Hau ~ hau ')
        func_as_param()
    return hau_nested

@sound_decorator
def pet_func():
    print('Pies to najlepszy przyjaciel człowieka')


pet_func()

