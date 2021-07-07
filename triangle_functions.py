def draw_row(height, row):
    draw_spaces(height, row)
    draw_increasing_numbers(row)
    draw_decreasing_numbers(row)


def draw_spaces(height, row):
    space = 2 * height - 2 * row
    while space > 0:
        print(end=" ")
        space = space - 1


def draw_increasing_numbers(row):
    number = 0
    while number <= row:
        print(number + 1, end=" ")
        number = number + 1


def draw_decreasing_numbers(row):
    number = row
    while 0 < number:
        print(number, end=" ")
        number = number - 1

    print()


def draw_triangle():
    height = input("Enter height: ")
    height = int(height)
    for row in range(height):
        draw_row(height, row)


draw_triangle()
