from main import return_answer


def parse_file():
    file = open("test.txt")
    line_number = 1
    problematic_lines = 0
    for line in file:
        if not parse_line(line, line_number):
            problematic_lines += 1
        line_number += 1

    if problematic_lines == 0:
        print("Hooray! You are the best!")


def parse_line(line, line_number):
    line = line.strip()
    divided_line = line.split(",")
    expected_result = divided_line[1]
    if expected_result == "Error please enter a number up to 10000.":
        actual_result = return_answer(expected_result)
        if expected_result != actual_result:
            print("There's a problem with line number {}. should have been: {}, but got: {}".format(line_number,
                                                                                                    expected_result,
                                                                                                    actual_result))
            return False
    else:
        number = int(divided_line[0])
        actual_result = return_answer(number)
        lower_actual_result = actual_result.lower()
        lower_actual_result = lower_actual_result.strip()
        if expected_result != lower_actual_result:
            print("There's a problem with line number {}. should have been: {}, but got: {}".format(line_number,
                                                                                                    expected_result,
                                                                                                    lower_actual_result))
            return False


parse_file()
