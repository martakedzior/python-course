def read_from(file):
    with open(file, 'r', encoding='utf-8') as fp:
        content = fp.read()
    return content


def find_longest(words_list):
    longest = ''
    for word in words_list:
        if len(word) > len(longest):
            longest = word
    return longest


text = read_from('text.txt')

for i in ['!', ',', '.', ';']:
    text = text.replace(i, '')

longest = find_longest(text.split())

print(longest)