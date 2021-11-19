"""
Import random integers to generate board ships and computer guesses
Time library used to make game realistic i.e pause for seconds several times.
"""
from random import randint
import time


class Board:
    """
    General strucuture for each player and board.
    Used to call board information throughout the game.
    Global score also used to keep score count.
    """
    score = 0

    def __init__(self, name, size, ship_nums, type):
        self.name = name
        self.size = size
        self.ship_nums = ship_nums
        self.type = type
        self.board = [['|  ' for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        """
        Adds and prints player and computer board.
        """
        for row in self.board:
            print(' '.join(row))

    def add_ships(self, x, y, type='computer'):
        """
        Adds ships to each board.
        For player, @ represents each ship
        For computer, they are hidden
        """
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
    to set up the game i.e size of the board and number of ships.
    Returns size and number of ships in a
    list form.
    The while stays active until the input validation function
    comes back true to prevent Key and Value error
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
    Checks if "values" is an integer and whether or not is
    in the given range (a - b)
    It will only return True if values is correct.
    """
    try:
        if values.isnumeric() is False:
            raise ValueError(
                f'You must enter a number.. you entered "{values}"\n'
            )
        elif int(values) < a or int(values) > b:
            print(f'Invalid Input: Number entered {values} is not in range\n')
            print('Please try again...')
            return False
    except ValueError as e:
        print(f'Invalid input: {e}\nPlease try again...\n')
        return False

    return True


def populate_game_board(board):
    """
    Based on data returned from get_user_data function.
    Using class function, adds number of ships to each board
    until number of ships match user input.
    Then populates game board for each player, one for the user
    and one for the computer.
    """
    print('~' * 60)
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
    For computer, generates random row and col coordanites.
    For player, row and col input is requested and validated.
    Size -1 given that rows and cols start with 0.
    Returns (row, col) in a list form as integers.
    """
    size = board.size
    while True:
        if board.type == 'computer':
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            print('~' * 60)
            row_guess = input('Enter row num:\n')
            col_guess = input('Enter column num:\n')
            print('~' * 60)

        row = validate_user_data(str(row_guess), 0, (size - 1))
        col = validate_user_data(str(col_guess), 0, (size - 1))

        if row and col:
            break

    return [int(row_guess), int(col_guess)]


def validate_guess(board, other_board, x, y):
    """
    Validates player input:
    Checks for duplicates within each board's guess list first.
    Checks if co-ords match other board's ship co-ords (hit).
    If none of the above, its a miss.
    """
    if (x, y) in board.guesses:
        print(f'{board.name}, you already guessed {(x, y)}.')
        print('Please try again...')
        time.sleep(2)
        return False

    if (x, y) in other_board.ships:
        board.guesses.append((x, y))
        other_board.board[x][y] = '| O'
        print(f"{board.name}'s coordinates {(x, y)}")
        time.sleep(2)
        print('A Battleship has been hit!')
        print('~' * 60)
        time.sleep(2)
        return True
    else:
        board.guesses.append((x, y))
        other_board.board[x][y] = '| X'
        print(f"{board.name}'s coordinates {(x, y)}")
        time.sleep(2)
        print('Missed target...')
        print('~' * 60)
        time.sleep(2)


def play_game(board, other_board, ships):
    """
    Runs the entire game until end phase.
    While loop used to run the game until number of rounds
    match number of ships chosen.
    If statements restart loop if input data is invalid.
    Updates global score for each board if ship hit.
    Displays end score and comments once while loop is broken.
    """
    while True:
        populate_game_board(board)
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
        if valid_two is False:
            board.guesses.pop()
            return play_game(board, other_board, ships)

        scores(board, valid)
        scores(other_board, valid_two)
        time.sleep(2)
        print('~' * 60)
        next_round = input('Press Enter to continue or "q" to quit.\n')
        if next_round == 'Enter':
            continue
        elif next_round == 'q':
            break
        if len(other_board.guesses) == ships:
            break
    print('~' * 60)
    print('Finishing game, few moments...')
    time.sleep(3)
    print('~' * 60)
    print(f"{board.name}'s score is: {board.score}")
    print(f"{other_board.name}'s score is: {other_board.score}\n")
    if board.score > other_board.score:
        print(f'{board.name} won this game.')
        print('Well done for defeating your opponent!')
    elif board.score < other_board.score:
        print(f'{other_board.name} won this game. Might be luckier next time')
    elif board.score == other_board.score:
        print('Both sides have taken damage but victory was on either side.')
        print('Well fought, might get luckier next time.')
    time.sleep(3)


def scores(board, hit):
    """
    If a ship is hit, updates class board score by adding 5.
    Once updated, prints board's name and updated score.
    """
    if hit:
        board.score += 5
        print(f"{board.name}'s score is: {board.score}")
    else:
        print(f"{board.name}'s score is: {board.score}")


def new_game():
    """
    Runs main game from start to finish.
    At finish, restarts or quits function based on user input.
    Includes end-game goodbye message.
    """
    print('~' * 60)
    print("              |    |    | ")
    print("             (_(  (_(  (_(")
    print("           /(___((___((___(")
    print("         //(____(____(_____(")
    print("     __///____|____|____|_____")
    print("---------(                   /---------")
    print("  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^")
    print("    ^^^^      ^^^^     ^^^    ^^")
    print("         ^^^^      ^^^\n")
    print('        WELCOME TO BATTLESHIPS')
    print('~' * 60)
    name = input('Please enter your name here:\n')
    time.sleep(0.5)
    print(f"Hi {name}. Let's go through some rules first...\n")
    time.sleep(1)
    print('~' * 60)
    print('1. Number of rounds will be equal to the number of ships you will chose.\n')
    print('2. Each ship sank is worth 5 points\n')
    print('3. Top left hand corner is row 0, col 0 (0, 0)\n')
    print('4. Number of rows will be equal to the number of columns')
    print('~' * 60)
    time.sleep(4)
    input('Press Enter to start your game.\n')
    print('Starting game...\n')
    time.sleep(2)
    data = get_user_data()
    size = int(data[0])
    num_of_ships = int(data[1])
    print(f'Remember, rows and columns will now range from "0 to {size - 1}"\n')
    time.sleep(2)
    print('Creating new game...\n')
    time.sleep(2)

    player_board = Board(name, size, num_of_ships, type='player')
    computer_board = Board('Computer', size, num_of_ships, type='computer')
    time.sleep(2)
    play_game(player_board, computer_board, num_of_ships)

    populate_game_board(player_board)

    populate_game_board(computer_board)
    print('~' * 60)
    print('Are you ready to challenge yourself again?\n')
    replay = input('Enter "y" to play another or "n" to quit the game:\n')
    if replay == 'y':
        new_game()
    else:
        print(f'Well played {player_board.name}. Goodbye for now!\n')


new_game()
