height = input("height: ")
height = int(height)
width = input("width: ")
width = int(width)

for row in range(height):
    for col in range(width):
        print("*", end="")
    print()