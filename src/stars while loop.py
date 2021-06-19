height = input("height: ")
height = int(height)
width = input("width: ")
width = int(width)

row = 0
while row < height:

    col = 0
    while col < width:
        print("*", end="")
        col = col + 1


    print()
    row = row + 1
