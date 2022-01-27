from main import is_formula_valid


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
    formula = divided_line[1]
    valid = divided_line[0]
    if valid == "true":
        valid = True
    else:
        valid = False

    if is_formula_valid(formula) != valid:
        print("There's a problem with line number", line_number)
        return False

    return True


parse_file()
