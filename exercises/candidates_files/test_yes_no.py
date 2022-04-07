from main import check_yes_no


def parse_file():
    file = open("test_yes_no.txt")
    line_number = 1
    problematic_lines = 0
    for line in file:
        if not parse_line(line, line_number):
            problematic_lines += 1
        line_number += 1

    if problematic_lines == 0:
        print("good job!")


def parse_line(line, line_number):
    line = line.rstrip()
    divided_line = line.split(",")
    valid = divided_line[1]
    answer = divided_line[0]
    if valid == "true":
        valid = True
    else:
        valid = False

    if check_yes_no(answer) != valid:
        print("There's a problem with line number", line_number)
        return False

    return True


parse_file()

