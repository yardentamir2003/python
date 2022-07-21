height = input("height: ")
height = int(height)
for row in range(height):
    for col in range(row+1):
        print(col+1, end="")
    print()
