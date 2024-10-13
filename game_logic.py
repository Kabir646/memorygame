import random
import time

class MemoryGame:
    def __init__(self, grid_size=4):  # Set grid size to 4x4
        self.grid_size = grid_size
        self.moves = 0
        self.first_click = None
        self.second_click = None
        self.board = []
        self.answer_board = []
        self.flipped_tiles = []
        self.is_processing = False
        self.create_board()

    def create_board(self):
        num_pairs = (self.grid_size * self.grid_size) // 2
        symbols = list('ABCDEFGH')[:num_pairs] * 2
        random.shuffle(symbols)

        self.answer_board = [symbols[i:i + self.grid_size] for i in range(0, len(symbols), self.grid_size)]
        self.board = [['' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.flipped_tiles = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.moves = 0
        self.first_click = None
        self.second_click = None

    def get_board(self):
        return self.board

    def flip_card(self, i, j):
        if i < 0 or j < 0 or i >= self.grid_size or j >= self.grid_size:
            return False

        if self.is_processing:
            return False

        if self.flipped_tiles[i][j]:
            return False

        if self.first_click is None:
            self.first_click = (i, j)
            self.board[i][j] = self.answer_board[i][j]
            self.flipped_tiles[i][j] = True
            return True
        elif self.second_click is None:
            self.second_click = (i, j)
            self.board[i][j] = self.answer_board[i][j]
            self.flipped_tiles[i][j] = True
            return True

    def reset_pair(self):
        i1, j1 = self.first_click
        i2, j2 = self.second_click
        self.board[i1][j1] = ''
        self.board[i2][j2] = ''
        self.flipped_tiles[i1][j1] = False
        self.flipped_tiles[i2][j2] = False
        self.first_click = None
        self.second_click = None

    def get_moves(self):
        return self.moves

    def check_match(self):
        i1, j1 = self.first_click
        i2, j2 = self.second_click

        self.is_processing = True
        if self.answer_board[i1][j1] == self.answer_board[i2][j2]:
            self.first_click = None
            self.second_click = None
            self.moves += 1
            self.is_processing = False
            return True
        else:
            self.moves += 1
            time.sleep(0.5)
            self.reset_pair()
            self.is_processing = False
            return False

    def is_game_over(self):
        for row in self.flipped_tiles:
            if False in row:
                return False
        return True
