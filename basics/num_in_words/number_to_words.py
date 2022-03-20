def main():
    number = input("Enter number: ")
    if len(number) == 1:
        word = one_digit(number)
        print(word)
    elif len(number) == 2:
        words = two_digit(number)
        print(words)


def one_digit(number):
    file = open("translator")
    for line in file:
        if line[0] == number:
            comma_position = line.find(",")
            return line[2:comma_position]


def two_digit(number):
    file = open("translator")
    for line in file:
        line = line.strip()
        comma_position = line.find(",")
        if number[0] == line[0]:
            dozens = line[comma_position:]
            for line in file:
                if line[0] == number[1]:
                    units_digit = line[0]
                    words = (dozens, units_digit)
                    return words


main()

