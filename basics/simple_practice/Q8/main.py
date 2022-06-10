import re


def main():
    file_name = input("Enter a file name: ")
    # if file_name.endswith(".txt"):

    if file_name.endswith(".numbers"):
        parse_file(file_name)


def parse_file(file_name):
    with open(file_name, "r") as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.strip()
            line = re.sub('[a-zA-Z]', '', line)
            words_list = line.split()
            average = calculate_average(words_list)
            print("line {}: {}".format(line_number, average))


def calculate_average(words_list):
    for i in range(0, len(words_list)):
        words_list[i] = int(words_list[i])
    total = sum(words_list)
    items = len(words_list)
    average = total / items
    return average


main()
