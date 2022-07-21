def main():
    file_name = input("Enter a file name: ")
    line_list = create_line_list(file_name)
    lines_with_digit = 0
    for line in line_list:
        if contains_number(line):
            lines_with_digit += 1
            print(line)
    lines_number = len(line_list)
    no_digit_lines = lines_number - lines_with_digit
    print("The file has {} lines, {} of them with numbers, and {} without numbers.".format(lines_number, lines_with_digit, no_digit_lines))


def create_line_list(file_name):
    line_list = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            line_list.append(line)
    return line_list


def contains_number(line):
    for character in line:
        if character.isdigit():
            return True
    return False


main()