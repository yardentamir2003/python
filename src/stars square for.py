height = input("height: ")
height = int(height)
width = input("width: ")
width = int(width)

for i in range(height):
    for j in range(width):
        print("*", end="")
    print()