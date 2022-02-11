from main import check_line


def parse_file():
    file = open("test.txt")
    line_number = 1
    problematic_lines = 0
    for line in file:
        if not parse_line(line, line_number):
            problematic_lines += 1
        line_number += 1

    if problematic_lines == 0:
        print("Hooray! Your code is spectacular!")


def parse_line(line, line_number):
    line = line.rstrip()
    divided_line = line.split(",")
    sentence = divided_line[0]


parse_file()