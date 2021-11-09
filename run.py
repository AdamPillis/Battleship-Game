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
    while True:
        print('Number of rows will be equal to the number of columns')
        print('Number must be between 5 and 10')
        size = input('Size of board: ')

        print('Number of ships must not exceed 10')
        ships = input('Number of ships: ')

        new_size = validate_user_data(size)
        new_ships = validate_user_data(ships)
        
        if new_size and new_ships:
            print('Data is valid')
            break
        
    return [size, ships]


def validate_user_data(values):
    """
    Checks if user input is an integer and whether or not is
    in the given range (5 - 10)
    If string, it raises ValueError
    """
    try:
        if int(values) < 5 or int(values) > 10:
            raise ValueError(
                f'Both numbers must be between 5 and 10, you entered {values}'
            )
    except ValueError as e:
        print(f'Invalid input: {e}, please try again...\n')
        return False

    return True


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
    data = get_user_data()
    print(data)


play_game()