import os
import re

blank_lines = 0
note_lines = 0
code_lines = 0
total_lines = 0


def get_files(path='./test'):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fp_path = path + '/' + fp
        if os.path.isfile(fp_path) and fp_path.endswith(".py"):
            files.append(fp_path)
        elif os.path.isdir(fp_path):
            files.extend(get_files(fp_path))
    return files


def process_file(filename):
    global total_lines
    global code_lines
    global note_lines
    global blank_lines
    with open(filename, 'r') as file:
        lines = file.readlines()
    note = '[(#)(//)(/*)(*)]'
    for line in lines:
        total_lines += 1
        if line.strip() == '':
            blank_lines += 1
        elif re.compile(note).match(line) is None:
            note_lines += 1
        else:
            code_lines += 1


def process():
    print(get_files())
    for file in get_files():
        process_file(file)
    print("total lines: ", total_lines)
    print("code lines: ", code_lines)
    print("comment lines: ", note_lines)
    print("blank lines: ", blank_lines)


process()
