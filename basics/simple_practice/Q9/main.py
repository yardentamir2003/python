# def main():
#     x_row = 0
#     x_col = 0
#     draw_board(x_row, x_col)
#     "quit" == False
#     while not "quit":
#         move = input("Enter your move: ")
#         try:
#             if move == "up":
#                 x_row += 1
#             if move == "down":
#                 x_row -= 1
#             if move == "right":
#                 x_col += 1
#             if move == "left":
#                 x_col -= 1
#             if move == "quit":
#                 print("Bye bye, have a nice day.")
#                 "quit" == True
#             else:
#                 print("Please enter: up, left, right, down, or quit.")
#         except:
#             print("Error: unable to move {}.".format(move))


def draw_board(x_row, x_col):
    for row in range(4):
        if row == x_row:
            if col == x_col:
                print("x")
        for col in range(4):
            print("o", end="")
        print()


draw_board(0,0)
