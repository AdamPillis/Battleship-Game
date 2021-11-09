from random import randint


class Board:
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

    def player_guess(self, width, height):
        self.guesses.append((width, height))
        self.board[width][height] = 'X'

        if (width, height) in self.ships:
            self.board[width][height] = '#'
            return f'{self.name}, you hit and sank a battleship!'

        else:
            return f"{self.name}, you've missed this time..."

    def add_ships(self, width, height, type='computer'):
        if len(self.ships) >= self.ship_nums:
            print('Too many ships')

        else:
            self.ships.append((width, height))
            if self.type == 'player':
                self.board[width][height] = '@'
