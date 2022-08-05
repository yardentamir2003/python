from chapter14.Q4.board import Board
import re


def main():
    board = Board()
    board.draw_board()
    while True:
        board_location = input("Enter the queen target destination: ")
        if board_location == "quit":
            print("Okay, bye bye.")
            exit(1)
        if not valid_board_location(board_location):
            print("{} is not a valid board location.".format(board_location))
            continue
        target_row, target_col = parse_location(board_location)

        if not board.valid_move(target_row, target_col):
            print("{} is not a valid move.".format(board_location))
            continue

        board.move(target_row, target_col)


def valid_board_location(board_location):
    match = re.findall('^[A-H][1-8]$', board_location)
    if len(match) == 0:
        return False
    return True


def parse_location(board_location):
    letter_to_col = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    letter = board_location[0]
    target_col = letter_to_col[letter]
    target_row = int(board_location[1])
    return target_row, target_col


main()
