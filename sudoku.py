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

