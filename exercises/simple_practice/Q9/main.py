import re


def main():
    x_row = 0
    x_col = 0
    draw_board(0, 0)
    while True:
        move = input("Enter your move: ")
        if valid_input(move):
            if valid_move(move, x_row, x_col):
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


def draw_board(x_row, x_col):
    for row in range(4):
        for col in range(4):
            if row == x_row and col == x_col:
                print("x", end="")
            else:
                print("o", end="")
        print()


def valid_input(move):
    match_input = re.findall('^(?:up|down|right|left|quit)$', move)
    if len(match_input) == 0:
        return False
    return True


def valid_move(move, x_row, x_col):
    if x_row == 0 and move == "up" or x_row == 3 and move == "down" or x_col == 0 and move == "left" or x_col == 3 and move == "right":
        print("Error: unable to move {}.".format(move))
        return False
    return True


main()
