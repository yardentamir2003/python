import re


def main():
    file_name = input("Enter a file name: ")
    if file_name.endswith(".txt"):
        parse_words_file(file_name)

    if file_name.endswith(".numbers"):
        parse_numbers_file(file_name)


def parse_words_file(file_name):
    with open(file_name, "r") as file:
        line_number = 0
        for line in file:
            line_number += 1
            line = line.strip()
            if not line.endswith("."):
                print("Line {}: {}".format(line_number, line))


def parse_numbers_file(file_name):
    with open(file_name, "r") as file:
        line_number = 0
        average_list = []
        for line in file:
            line_number += 1
            line = line.strip()
            line = re.sub('[a-zA-Z]', '', line)
            words_list = line.split()
            average = calculate_average(words_list)
            average_list.append(average)
            print("line {}: {}".format(line_number, average))
        average_of_all = calculate_average(average_list)
        print("The average of all the averages is: {}".format(average_of_all))


def calculate_average(my_list):
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])
    total = sum(my_list)
    items = len(my_list)
    average = total / items
    return average


main()
