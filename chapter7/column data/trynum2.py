def read_lines(column_name):
    answers = []
    file_input = open("input.csv", "r")
    first_line = True
    for line in file_input:
        if first_line:
            columns_names = parse_line(line)
            first_line = False
            continue
        else:
            columns = parse_line(line)
            num = find_index(column_name, columns_names)
            answer = columns[num]
            answers.append(answer)

    return answers


def find_index(column_name, columns_names):
    index = 0
    while index < len(columns_names):
        if column_name.lower() == columns_names[index].lower():
            break
        else:
            index = index + 1

    return index


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


name = input("Enter a column name: ")
data = read_lines(name)
for value in data:
    print(value)
