def main():
    row_queen = 1
    col_queen = 1
    draw_board(row_queen, col_queen)


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


main()