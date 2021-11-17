"""
To import random numbers to generate ships and computer guesses
"""
from random import randint
import time


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
        self.board = [['|  ' for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def board_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

    def add_ships(self, x, y, type='computer'):
        while (x, y) not in self.ships:
            self.ships.append((x, y))

            if self.type == 'player':
                self.board[x][y] = '| @'


def random_number(size):
    """
    Returns random integer between 0 and the length of the board
    chosen by the player.
    """
    return randint(0, (size) - 1)


def get_user_data():
    """
    Collects information from user which is required
    to set up the game i.e size of the board.
    Returns width, height and number of ships in a
    list form.
    """
    while True:
        print('Numbers must be between 5 and 10\n')
        size = input('Size of your square board:\n')
        print('Validating input...\n')
        time.sleep(1)

        new_size = validate_user_data(size, 5, 10)

        if new_size:

            ships = input('Number of ships on each board:\n')
            print('Validating input...\n')
            time.sleep(1)

            new_ships = validate_user_data(ships, 5, 10)

            if new_ships:
                break

    return [size, ships]


def validate_user_data(values, a, b):
    """
    Checks if user input is an integer and whether or not is
    in the given range (5 - 10)
    If string, it raises ValueError
    """
    try:
        if values.isnumeric() is False:
            raise ValueError(
                f'You must enter a number.. you entered {values}'
            )
        elif int(values) < a or int(values) > b:
            print(f'Invalid Input: Number entered {values} is not in range\n')
            print('Please try again...\n')
            return False
    except ValueError as e:
        print(f'Invalid input: {e}, please try again...\n')
        return False

    return True


def populate_game_board(board):
    """
    Populates game board for each player, one for the user
    and one for the computer. Size and number of ships depends on
    user input
    """
    print(f"{board.name}'s board:\n")

    size = board.size

    while len(board.ships) != board.ship_nums:
        x = random_number(size)
        y = random_number(size)
        board.add_ships(x, y)

    board.print_board()
    print(board.ships)


def make_guess(board):
    """
    For computer, generates random x and y coordanites.
    For player, row and col input is requested.
    """
    size = board.size
    while True:
        if board.type == 'computer':
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            row_guess = input('Enter row num:\n')
            col_guess = input('Enter column num:\n')

        row = validate_user_data(str(row_guess), 0, (size - 1))
        col = validate_user_data(str(col_guess), 0, (size - 1))

        if row and col:
            break

    return [int(row_guess), int(col_guess)]


def validate_guess(board, other_board, x, y):
    """
    Validates player input: Must be number within range,
    checks for duplicates and whether a ship is hit or not.
    """ 
    if (x, y) in board.guesses:
        print(f'{board.name}, you already guessed {(x, y)}.')
        print('Please try again.')
        return False

    if (x, y) in other_board.ships:
        board.guesses.append((x, y))
        other_board.board[x][y] = '| O'
        print('~' * 60)
        print(f"{board.name}'s coordinates {(x, y)}")
        time.sleep(1)
        print('A Battleship has been hit!\n')
        return True
    else:
        board.guesses.append((x, y))
        other_board.board[x][y] = '| X'
        print('~' * 60)
        print(f"{board.name}'s coordinates {(x, y)}")
        time.sleep(1)
        print('Missed target...\n')
        return True


def play_game(board, other_board, ships):
    """
    """
    while True:
        populate_game_board(board)
        print('~' * 50)
        populate_game_board(other_board)

        player_guess = make_guess(board)
        p_row = player_guess[0]
        p_col = player_guess[1]
        valid = validate_guess(board, other_board, p_row, p_col)
        if valid is False:
            return play_game(board, other_board, ships)

        comp_guess = make_guess(other_board)
        c_row = comp_guess[0]
        c_col = comp_guess[1]
        valid_two = validate_guess(other_board, board, c_row, c_col)
        scores(board, valid)
        scores(other_board, valid_two)

        if len(other_board.guesses) == ships:
            break
    print('finished play game')


def scores(board, hit):
    """
    """
    board_score = 0

    if hit:
        board_score += 5
        print('~' * 60)
        print(f"{board.name}'s score is now: {board_score}")


def new_game():
    """
    Runs main game every time user reloads
    or restarts the game
    """
    print('~' * 60)
    print('WELCOME TO BATTLESHIPS')
    print('~' * 60)
    name = input('Please enter your name here:\n')
    time.sleep(0.5)
    print(f"Hi {name}. Let's go through some rules first...\n")
    time.sleep(1)
    print('~' * 60)
    print('1. Number of rounds will be equal to the number of ships chosen.\n')
    print('2. Each ship sank is worth 5 points\n')
    print('3. Top left hand corner is row 0, col 0\n')
    print('4. Number of rows will be equal to the number of columns')
    print('~' * 60)
    # time.sleep(5)
    input('Press Enter to start your game.\n')
    data = get_user_data()
    size = int(data[0])
    num_of_ships = int(data[1])
    print(f'Remember, rows and columns will now range from 0 to {size - 1}\n')
    time.sleep(2)
    print('Creating new game...\n')
    time.sleep(2)

    player_board = Board(name, size, num_of_ships, type='player')
    computer_board = Board('Computer', size, num_of_ships, type='computer')
    time.sleep(2)
    play_game(player_board, computer_board, num_of_ships)

    populate_game_board(player_board)
    print('~' * 60)
    populate_game_board(computer_board)
    print('game over')


new_game()