def main():
    number = input("Enter number: ")
    if len(number) == 1:
        unit = unit_digit(number)
        print(unit)
    elif len(number) == 2:
        unit = unit_digit(number)
        dozens = dozen_digit(number)
        print(dozens, unit)
    elif len(number) == 3:
        unit = unit_digit(number)
        dozens = dozen_3_digit(number)
        hundreds = hundred_digit(number)
        print(hundreds, "hundreds and", dozens, unit)


def unit_digit(number):
    file = open("translator")
    for line in file:
        if line[0] == number[-1]:
            comma_position = line.find(",")
            unit = line[2:comma_position]
            return unit


def dozen_digit(number):
    file = open("translator")
    for line in file:
        line = line.strip()
        comma_position = line.find(",")
        if number[0] == line[0]:
            dozens = line[comma_position+1:]
            return dozens


def dozen_3_digit(number):
    file = open("translator")
    for line in file:
        line = line.strip()
        comma_position = line.find(",")
        if number[1] == line[0]:
            dozens = line[comma_position + 1:]
            return dozens


def hundred_digit(number):
    file = open("translator")
    for line in file:
        line = line.strip()
        comma_position = line.find(",")
        if number[0] == line[0]:
            hundreds = line[2:comma_position]
            return hundreds


main()

#problems:
#always prints "zero" : 90 = ninety zero
#cant read special 2 digits : 14 = four, 312 = three hundreds and two
