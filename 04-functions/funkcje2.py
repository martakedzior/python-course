def ask_about_mood():
    question = 'How are you??'
    print(question)


def show(user_response):
    print('^^^^', user_response, '^^^')


def multiply_sentence(counter):
    sentence = "I love Python"
    return sentence * counter

def multiply(quote, counter):
    return (quote + '!') * counter


# main part of the code
print('***********')
ask_about_mood()

response = input('---> anwser here: ')
show(response)

exclamation = multiply_sentence(5)
print(exclamation)

quote1 = multiply("It's not a bug!", 2)
print(quote1)

print('-----END-----')