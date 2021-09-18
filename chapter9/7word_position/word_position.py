import re


def main():
    file_dictionary = dict()
    file = open("input.txt")
    line_number = 0
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = re.sub('[.,!?]', "", line)
        line = line.rstrip()
        parse_line(file_dictionary, line, line_number)
        line_number += 1


def parse_line(file_dictionary, line, line_number):
    words = line.split(" ")
    word_number = 0
    for word in words:
        if word not in file_dictionary:
            val = "line {} word {}".format(line_number + 1, word_number + 1)
            file_dictionary[word] = [val]
        else:
            word_number += 1
            # val = "line " + str(line_number) + "word " + str(word_number)
            val = "line {} word {}".format(line_number + 1, word_number + 1)
            file_dictionary[word].append(val)

    for word in file_dictionary:
        print(word, end=" : ")
        values = file_dictionary[word]
        for item in values:
            print(item, end=" ")
        print()


main()
