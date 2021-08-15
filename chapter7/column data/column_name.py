def read_lines(column_name):
    answers = []
    file_input = open("input.csv", "r")
    first_line = True
    for line in file_input:
        if first_line:
            first_line = False
            continue
        else:
            columns = parse_line(line)
            if column_name == "first name":
                answer = columns[0]
            elif column_name == "last name":
                answer = columns[1]
            elif column_name == "age":
                answer = columns[2]
            elif column_name == "street number" or column_name == "street":
                answer = columns[3]
            elif column_name == "weight":
                answer = columns[4]
        answers.append(answer)
    return answers


def parse_line(line):
    words = []
    word = ""
    wait_for_start = True
    no_quotes = False
    with_quotes = False
    after_quotes = False
    for char in line:
        if after_quotes:
            if char == ",":
                after_quotes = False
                word = ""

        elif char == "\n":
            words.append(word)
            word = ""
            wait_for_start = True
            no_quotes = False
            with_quotes = False

        elif wait_for_start:
            wait_for_start = False
            if char == '"':
                with_quotes = True
            else:
                no_quotes = True
                word = word + char

        elif with_quotes:
            if char == '"':
                words.append(word)
                word = ""
                wait_for_start = True
                no_quotes = False
                with_quotes = False
                after_quotes = True
            else:
                word = word + char

        elif no_quotes:
            if char == ',':
                words.append(word)
                word = ""
                wait_for_start = True
                no_quotes = False
                with_quotes = False
            else:
                word = word + char

    return words


column_name = input("Enter a column name: ")
data = read_lines(column_name)
for answer in data:
    print(answer)
