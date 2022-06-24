import re


def main():
    row_queen = 1
    col_queen = 1
    draw_board(row_queen, col_queen)
    while True:
        board_location = input("Enter the queen target destination: ")
        if not valid_board_location(board_location):
            print("{} is not a valid board location.".format(board_location))
            continue
        target_row,target_col = parse_location(board_location)
        if not valid_move(row_queen, col_queen,target_row,target_col):
            print("{} is not a valid move.".format(board_location))
            continue

        row_queen,col_queen=target_row,target_col

        while col_queen<target_col:
            col_queen+=1
            draw_board(row_queen, col_queen)
        # loop col_queen<target_col:
        #     +1
        #     draw_board(row_queen, col_queen)



def draw_board(row_queen, col_queen):
    row_numbers = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    col_numbers = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
    for row in range(8, -1, -1):
        # print("row:", row)
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


def valid_move(row_queen, col_queen,target_row,target_col):
    # move right
    if target_col


def parse_location(board_location):
    letter_to_col = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
    letter = board_location[0]
    target_col = letter_to_col[letter]
    target_row = board_location[1]
    return target_row, target_col


main()