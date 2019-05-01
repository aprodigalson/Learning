import glob
from collections import Counter
import re
import string
import os
import nltk


# nltk.download('averaged_perceptron_tagger')


# get all txt file
def list_txt():
    return glob.glob("*.txt")


# word count ,but didn't ignore some  article like 'the' 'to' e.g.
def wordcount(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub("[\",.]", "", line)
            datalist.extend(content.strip().split(' '))

    return Counter(datalist).most_common(1)


# can replace by map(wordcount,list_text())
def most_comm():
    all_txt = list_txt()
    for txt in all_txt:
        print(wordcount(txt))


# if __name__ == "__main__":
#     most_comm()


# replace like "it's" to "it is"
def extend_word(text):
    if text.find('\'') > 0:
        old2new = dict()
        words = text.split()
        for word in words:
            if word.find('\'') > 0:
                parts = word.split('\'')
                if parts[1] == 'm':
                    parts[1] = 'am'
                elif parts[1] == 's':
                    parts[1] = 'is'
                elif parts[1] == 're':
                    parts[1] = 'are'
                elif parts[1] == 't':
                    parts[1] = 'not'

                old2new[word] = ' '.join(parts)
        _text = text
        for old_word in old2new.keys():
            _text = _text.replace(old_word, old2new[old_word])
        return _text


# get the most frequent noun
def show_important_word(records):
    items = sorted(records.items(), key=lambda x: x[1], reverse=True)
    freq = 0
    for item in items:
        # get the part of speech, return tag and word tuple,
        # if tag equals "NN" ,means that word is a noun
        word, tag = nltk.pos_tag([item[0]])[0]
        if tag.startswith('NN'):
            if item[1] < freq:
                return
            print(word)
            freq = item[1]
    if not freq:
        print(items[0][0])


# process one file
def process_file(filename):
    with open(filename, 'r') as file:
        article = file.read()
        no_pun_text = article
        _punctuation = string.punctuation.replace('\'', '')
        for pun in _punctuation:
            no_pun_text = no_pun_text.replace(pun, '')
        complete_text = extend_word(no_pun_text)
        records = dict()
        for word in complete_text.lower().split():
            records[word] = records.get(word, 0) + 1
        print('='*20)
        print('current file:', filename)
        print('-'*20)
        show_important_word(records)


def process_files(path='.'):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.txt'):
            process_file(os.path.join(path, file))


process_files()
