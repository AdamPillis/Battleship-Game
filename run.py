from random import randint


class main_board:
    """
    Will create player and computer board based on
    user input.
    """
    def __init__(self, name, size, ship_nums, type):
        self.name = name
        self.size = size
        self.ship_nums = ship_nums
        self.type = type
        self.board = [['~' for width in range(size)] for height in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        for row in board:
            print(' '.join(row))

