import re


def main():
    file = open("input.txt")
    line_number = 1
    for line in file:
        line = line.rstrip()
        x = re.findall('[bd][oe]?.$', line)
        if len(x) > 0:
            print("Sentence #", line_number, "is valid")
        else:
            word_number, problem = find_problem(line)
            print("Sentence #", line_number, "is invalid: word #", word_number, problem)
        line_number += 1
        main()


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