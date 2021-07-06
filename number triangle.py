height = input("Enter height: ")
height = int(height)

for row in range(height):
    space = 2*height-2*row
    while space > 0:
        print(end=" ")
        space = space - 1

    number = 1
    while number < row+1:
        print(number, end=" ")
        number = number + 1

    while number > 0:
        print(number, end=" ")
        number = number - 1
    row = row + 1
    print()
