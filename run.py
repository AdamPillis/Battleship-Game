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


def get_user_data():
    """
    Collects information from user which is required
    to set up the game i.e size of the board.
    Returns width, height and number of ships in a
    list form.
    """
    print('Number of rows and columns must be between 3 and 10.')
    width = input('Number of rows: ')
    height = input('Number of columns: ')
    ships = input('Number of ships: ')


def play_game():
    """
    Runs main game every time user reloads
    or restarts the game
    """
    print('~' * 60)
    print('WELCOME TO BATTLESHIPS')
    print('~' * 60)
    name = input('Please enter your name here: ')
    print(f"Hi {name}. Some rules before we start...")
    get_user_data()


play_game()
