import re


# use re to match the word
def word_count(filename):
    with open(filename, 'r') as fp:
        line = fp.read()
    words = re.findall(r'[\w\-_.\']+', line)
    print(len(words))


word_count("english.txt")
