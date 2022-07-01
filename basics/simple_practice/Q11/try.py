import re
import time


def move_right(row_queen, col_queen, target_col):
    while col_queen < target_col:
        col_queen += 1
        draw_board(row_queen, col_queen)
        if col_queen == target_col:
            print("The queen rests.")
        else:
            print("The queen is still moving…")
            time.sleep(1)
    return col_queen


def move_left(row_queen, col_queen, target_col):
    while col_queen > target_col:
        col_queen -= 1
        draw_board(row_queen, col_queen)
        if col_queen == target_col:
            print("The queen rests.")
        else:
            print("The queen is still moving…")
            time.sleep(1)
    return col_queen


def move_up(row_queen, col_queen, target_row):
    while row_queen < target_row:
        row_queen += 1
        draw_board(row_queen, col_queen)
        if row_queen == target_row:
            print("The queen rests.")
        else:
            print("The queen is still moving…")
            time.sleep(1)
    return row_queen


def move_down(row_queen, col_queen, target_row):
    while row_queen > target_row:
        row_queen -= 1
        draw_board(row_queen, col_queen)
        if row_queen == target_row:
            print("The queen rests.")
        else:
            print("The queen is still moving…")
            time.sleep(1)
    return row_queen


def main():
    row_queen = 1
    col_queen = 1
    draw_board(row_queen, col_queen)
    while True:
        board_location = input("Enter the queen target destination: ")
        if board_location == "quit":
            print("Okay, bye bye.")
            exit(1)
        if not valid_board_location(board_location):
            print("{} is not a valid board location.".format(board_location))
            continue
        target_row, target_col = parse_location(board_location)
        move = valid_move(row_queen, col_queen, target_row, target_col)

        if not valid_move(row_queen, col_queen, target_row, target_col):
            print("{} is not a valid move.".format(board_location))
            continue
        if move == "right":
            col_queen = move_right(row_queen, col_queen, target_col)
        elif move == "left":
            col_queen = move_left(row_queen, col_queen, target_col)
        elif move == "up":
            row_queen = move_up(row_queen, col_queen, target_row)
        elif move == "down":
            row_queen = move_down(row_queen, col_queen, target_row)


def draw_board(row_queen, col_queen):
    row_numbers = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    col_numbers = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
    for row in range(8, -1, -1):
        for col in range(9):
            if col == col_queen and row == row_queen:
                print("x", end="")
                continue
            if col == 0:
                print(row_numbers[row], end="")
                continue
            if row == 0:
                print(col_numbers[col], end="")
            else:
                print("o", end="")
        print()


def valid_board_location(board_location):
    match = re.findall('^[A-H][1-8]$', board_location)
    if len(match) == 0:
        return False
    return True


def valid_move(row_queen, col_queen, target_row, target_col):
    if target_col > col_queen and target_row == row_queen:
        return "right"
    elif target_col < col_queen and target_row == row_queen:
        return "left"
    elif target_col == col_queen and target_row > row_queen:
        return "up"
    elif target_col == col_queen and target_row < row_queen:
        return "down"
    else:
        return False


def parse_location(board_location):
    letter_to_col = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    letter = board_location[0]
    target_col = letter_to_col[letter]
    target_row = int(board_location[1])
    return target_row, target_col


main()
