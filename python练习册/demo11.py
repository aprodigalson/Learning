import re


def filter_word(text):
    word_filter = set()
    with open('filtered_words.txt', 'r', encoding='utf-8') as file:
        for x in file.readlines():
            word_filter |= {x.strip('\n')}

    with open('filtered_words.txt', 'r', encoding='utf-8') as file:
        f = file.read()
    _text = text

    if _text == '':
        print('Human Rights!')
    elif len(re.findall(r'%s' % _text, f)) == 0:
        print('Human Rights!')
        # demo12
        for x in word_filter:
            if x in _text:
                if x.isalnum():
                    _text = _text.replace(x, '*'*len(x))
                else:
                    _text = _text.replace(x, '*' * int(len(x)/2))
        print(_text)

    else:
        print('Freedom!')


# todo if input chinese ,this will be error
temp = input('>')
filter_word(temp)
