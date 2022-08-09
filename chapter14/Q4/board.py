import time


class Board:
    def __init__(self):
        self.col_queen = 1
        self.row_queen = 1

    def draw_board(self):
        row_numbers = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
        col_numbers = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        for row in range(8, -1, -1):
            for col in range(9):
                if col == self.col_queen and row == self.row_queen:
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

    def move_down_right(self, target_row, target_col):
        while self.col_queen < target_col and self.row_queen > target_row:
            self.col_queen += 1
            self.row_queen -= 1
            self.draw_board()
            if self.col_queen == target_col and self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def valid_move(self, target_row, target_col):
        if target_col > self.col_queen and target_row == self.row_queen:
            return "right"
        elif target_col < self.col_queen and target_row == self.row_queen:
            return "left"
        elif target_col == self.col_queen and target_row > self.row_queen:
            return "up"
        elif target_col == self.col_queen and target_row < self.row_queen:
            return "down"
        elif target_col - self.col_queen == target_row - self.row_queen:
            if self.col_queen < target_col and self.row_queen < target_row:
                return "up right"
            else:
                return "down left"
        elif self.col_queen + self.row_queen == target_col + target_row:
            if self.col_queen > target_col and self.row_queen < target_row:
                return "up left"
            else:
                return "down right"
        else:
            return False

    def move(self, target_row, target_col, board_location):
        direction = self.valid_move(target_row, target_col)
        if not direction:
            print("{} is not a valid move.".format(board_location))
            return
        if direction == "right":
            self.move_right(target_col)
        elif direction == "left":
            self.move_left(target_col)
        elif direction == "up":
            self.move_up(target_row)
        elif direction == "down":
            self.move_down(target_row)
        elif direction == "up right":
            self.move_up_right(target_row, target_col)
        elif direction == "down left":
            self.move_down_left(target_row, target_col)
        elif direction == "up left":
            self.move_up_left(target_row, target_col)
        elif direction == "down right":
            self.move_down_right(target_row, target_col)
        self.draw_board()

    def move_up_left(self, target_row, target_col):
        while self.col_queen > target_col and self.row_queen < target_row:
            self.col_queen -= 1
            self.row_queen += 1
            self.draw_board()
            if self.col_queen == target_col and self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_down_left(self, target_row, target_col):
        while self.col_queen > target_col and self.row_queen > target_row:
            self.col_queen -= 1
            self.row_queen -= 1
            self.draw_board()
            if self.col_queen == target_col and self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_up_right(self, target_row, target_col):
        while self.col_queen < target_col and self.row_queen < target_row:
            self.col_queen += 1
            self.row_queen += 1
            self.draw_board()
            if self.col_queen == target_col and self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_right(self, target_col):
        while self.col_queen < target_col:
            self.col_queen += 1
            self.draw_board()
            if self.col_queen == target_col:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_left(self, target_col):
        while self.col_queen > target_col:
            self.col_queen -= 1
            self.draw_board()
            if self.col_queen == target_col:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_up(self, target_row):
        while self.row_queen < target_row:
            self.row_queen += 1
            self.draw_board()
            if self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)

    def move_down(self, target_row):
        while self.row_queen > target_row:
            self.row_queen -= 1
            self.draw_board()
            if self.row_queen == target_row:
                print("The queen rests.")
            else:
                print("The queen is still moving…")
                time.sleep(1)
