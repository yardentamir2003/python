def main():
    x_row = 0
    x_col = 0
    draw_board(0, 0)
    while True:
        move = input("Enter your move: ")

            if x_row == 0 and move == "up" or x_row == 3 and move == "down" or x_col == 0 and move == "left" or x_col == 3 and move == "right":
                print("Error: unable to move {}.".format(move))
                continue
            if move == "up":
                x_row -= 1
            if move == "down":
                x_row += 1
            if move == "right":
                x_col += 1
            if move == "left":
                x_col -= 1

            if move == "quit":
                print("Bye bye, have a nice day.")
                break
            draw_board(x_row, x_col)
            else:
                print("Please enter: up, left, right, down, or quit.")
                draw_board(0, 0)


def draw_board(x_row, x_col):
    for row in range(4):
        for col in range(4):
            if row == x_row and col == x_col:
                print("x", end="")
            else:
                print("o", end="")
        print()


main()
