import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def make_move(self, board, row, col, value):
        if is_valid(board, value, (row, col)):
            board[row][col] = value
            self.score += 1
            return True
        return False
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None
