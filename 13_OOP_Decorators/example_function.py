def example_function():

    def nested_function():
        print('Jestem w srodku zagnieżdżenia')

    return nested_function


new_function = example_function()

new_function()