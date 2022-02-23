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
    expected_result = divided_line[1]
    actual_result = check_line(divided_line[0])
    if expected_result == "valid":
        if actual_result is not None:
            print("There's a problem with line number {}. should have been valid, but got: {}".format(line_number,
                                                                                                      actual_result))
            return False

    else:
        if expected_result != actual_result:
            print("There's a problem with line number {}. should have been: {}, but got: {}".format(line_number,
                                                                                                expected_result,
                                                                                                actual_result))
            return False

    return True


parse_file()
