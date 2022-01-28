import re


def main():
    file = open("input.txt")
    line_number = 1
    for line in file:
        line = line.rstrip()

    line_number += 1


def find_problem(line):
    word_number = 1
    for word in line:
        if:
        problem = "is invalid"
        elif:
        problem = "is already exists"
        else:
        problem = "missing dot at the end"

    return word_number, problem


def missing_dot(line):
    dot_exists = re.findall('\\.$', line)
    problem = "missing dot at the end."
    return len(dot_exists) > 0, problem

def bdoe_letters(line):
    bdoe_only = re.findall('(b[bdoe]*)|(d[bdoe]*)|([bdoe]*b)|([bdoe]*d)', line)
    return len(bdoe_only) > 0, ""

def word_twice(line):
    word_number = 1
    words = line.split()
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = 1
        else:
            problem = ("word #", word_number, "is already exists.")
            return False, problem
        word_number += 1

def longer_word(line):
