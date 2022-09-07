def draw_arrow(num):
    for row in range(num):
        for col in range(row + 1):
            print('*', end=" ")
        print("\n", end="")

    for row in range(num - 1):
        for col in range(num - 1 - row):
            print('*', end=" ")
        print("\n", end="")


draw_arrow(5)
