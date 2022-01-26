from main import is_formula_valid


def parse_line():
    file = open("test.txt")
    line_number = 1
    for line in file:
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
        else:
            print("Hooray! Your code is spectacular!")
        line_number += 1


parse_line()