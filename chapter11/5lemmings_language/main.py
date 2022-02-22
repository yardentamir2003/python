import re


def main():
    file = open("input.txt")
    sentence_number = 1
    for line in file:
        line = line.rstrip()
        problem = check_line(line)
        if problem is None:
            print("sentence #{} is valid.".format(sentence_number))
        else:
            print("sentence #{} is invalid: {}".format(sentence_number, problem))
        sentence_number += 1


def check_line(line):
    problem = ends_with_dot(line)
    if problem is not None:
        return problem
    problem = word_twice(line)
    if problem is not None:
        return problem
    problem = longer_than_previous(line)
    if problem is not None:
        return problem
    problem = bdoe_letters(line)
    if problem is not None:
        return problem
    problem = eo_amount(line)
    if problem is not None:
        return problem


def ends_with_dot(line):
    match = re.findall('\\.$', line)
    if len(match) == 0:
        return "missing dot at the end."


def word_twice(line):
    word_number = 1
    words = line.split()
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = 1
        else:
            return "word #{} already exists.".format(word_number)
        word_number += 1


def longer_than_previous(line):
    index = 0
    words = line.split()
    while index < len(words) - 1:
        if len(words[index]) > len(words[index + 1]):
            return "word #{} is invalid".format(index)
        else:
            index += 1


def bdoe_letters(line):
    line = re.sub('[.]', '', line)
    words = line.split()
    word_number = 1
    for word in words:
        match = re.findall('^[bdoe][bdoe]*$', word)
        if len(match) == 0:
            return "word #{} is invalid".format(word_number)
        word_number += 1


def eo_amount(line):
    line = re.sub('[.]', '', line)
    word_number = 1
    words = line.split()
    for word in words:
        pattern = '(^[bd]*(e{{{}}})?[bd]*(o{{{}}})?[bd]*$)|(^[bd]*(o{{{}}})?[bd]*(e{{{}}})?[bd]*$)'.format(word_number, word_number, word_number, word_number)
        #יש פה טעות
        match = re.findall(pattern, word)
        if len(match) == 0:
            return "word #{} is invalid.".format(word_number)
        word_number += 1


if __name__ == '__main__':
    main()
