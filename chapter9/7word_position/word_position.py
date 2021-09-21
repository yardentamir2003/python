import re


def main():
    file_dictionary = {}
    file = open("input.txt")
    line_number = 0
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = re.sub('[.,!?]', "", line)
        parse_line(file_dictionary, line, line_number)
        line_number += 1
    print_output(file_dictionary)


def parse_line(file_dictionary, line, line_number):
    words = line.split(" ")
    word_number = 0
    for word in words:
        val = "line {} word {}".format(line_number + 1, word_number + 1)

        if word in file_dictionary:
            file_dictionary[word].append(val)
        else:
            file_dictionary[word] = [val]

        word_number += 1


def print_output(file_dictionary):
    for word in file_dictionary:
        print(word, end=" : ")
        location_list = file_dictionary[word]
        for item in location_list:
            print(item, end=" ")
        print()


main()
