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


draw_board()