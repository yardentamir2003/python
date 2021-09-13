def print_word(word_number, word_list):
    if word_number < len(word_list):
        word = word_list[word_number]
        print(word, end=" ")
    else:
        print("X", end=" ")


def print_line(line_number, line_list, first_word, width):
    line = ""
    if line_number < len(line_list):
        line = line_list[line_number]

    word_list = line.split(" ")
    for i in range(width):
        word_number = i + first_word
        print_word(word_number, word_list)

    print()


def rectangle_creator(numbers):
    num_list = numbers.split(" ")
    first_line = int(num_list[0])
    first_word = int(num_list[1])
    width = int(num_list[2])
    height = int(num_list[3])

    file = open("input.txt")
    file_lines = []
    for line in file:
        line = line.rstrip()
        file_lines.append(line)

    for i in range(height):
        line_number = i + first_line
        print_line(line_number, file_lines, first_word, width)


def story_square():
    numbers = input("Enter 4 numbers:")
    rectangle_creator(numbers)


story_square()
