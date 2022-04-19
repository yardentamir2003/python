from main import valid_flight_number


def parse_line(line, line_number):
    line = line.rstrip()
    divided_line = line.split(",")
    valid = divided_line[1]
    flight_number = divided_line[0]
    if valid == "true":
        valid = True
    else:
        valid = False

    if valid_flight_number(flight_number) != valid:
        print("There's a problem with line number", line_number)
        return False

    return True


def parse_file():
    file = open("test_flight_number.txt")
    line_number = 1
    problematic_lines = 0
    for line in file:
        if not parse_line(line, line_number):
            problematic_lines += 1
        line_number += 1

    if problematic_lines == 0:
        print("Roses are red.\n"
              "Violets are blue.\n"
              "Python is great.\n"
              "And so are you.\n")


parse_file()
