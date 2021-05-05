# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
from time import process_time, sleep

def timepassed(func):
    def nested():
        start = process_time()
        func()
        end = process_time()
        result = end - start
        print(result)

    return nested

@timepassed
def example_function():
    print('start')
    sleep(5)
    print('koniec')

@timepassed
def example_2():
    var = 4 + 5
    return var * 40

example_function()
example_2()