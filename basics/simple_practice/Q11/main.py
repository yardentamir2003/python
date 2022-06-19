import re


def main():
    draw_board()
    while True:
        board_location = input("Enter the queen target destination: ")
        if valid_board_location(board_location):
            if valid_move(board_location):
                break
            print("{} is not a valid move.".format(board_location))
        print("{} is not a valid board location.".format(board_location))


def draw_board():
    row_numbers = ["8", "7", "6", "5", "4", "3", "2", "1", " "]
    col_numbers = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
    for row in range(9):
        for col in range(9):
            if col == 0:
                print(row_numbers[row], end="")
                continue
            if row == 8:
                print(col_numbers[col], end="")
            else:
                print("o", end="")
        print()


def valid_board_location(board_location):
    match = re.findall('^[A-H][1-8]$', board_location)
    if len(match) == 0:
        return False
    return True


def valid_move(board_location):


main()