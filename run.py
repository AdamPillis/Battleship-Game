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
        self.board = [['| ' for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def board_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = '#'
            return f'{self.name}, you hit and sank a battleship!'
        else:
            return f"{self.name}, you've missed this time..."

    def add_ships(self, x, y, type='computer'):
        if len(self.ships) >= self.ship_nums:
            print('Too many ships')

        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = '@'


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
        print('Number of rows will be equal to the number of columns')
        print('Numbers must be between 5 and 10\n')
        size = input('Size of board:\n')

        ships = input('Number of ships:\n')

        new_size = validate_user_data(size, 5, 10)
        new_ships = validate_user_data(ships, 5, 10)

        if new_size and new_ships:
            print('Data is valid\n')
            break

    return [size, ships]


def validate_user_data(values, a, b):
    """
    Checks if user input is an integer and whether or not is
    in the given range (5 - 10)
    If string, it raises ValueError
    """
    try:
        if int(values) < a or int(values) > b:
            raise ValueError(
                f'Both numbers must be between 5 and 10, you entered {values}'
            )
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
            print("Computer's turn to guess")
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            row_guess = int(input('Enter row num:\n'))
            col_guess = int(input('Enter column num:\n'))

        row = validate_user_data(row_guess, 0, size)
        col = validate_user_data(col_guess, 0, size)

        if row and col:
            break

    return [int(row_guess), int(col_guess)]


def validate_guess(board, other_board, x, y):
    """
    Validates player input: Must be number within range,
    checks for duplicates and whether a ship is hit or not.
    """
    ships_to_hit = other_board.ships
    board_guesses = board.guesses
    while True:
        for board_guess in board_guesses:
            if (x, y) == board_guess:
                print(f'{board.name}, you already guessed {guess}.')
                print('Please try again.')
                return False

        break

    for ship_to_hit in ships_to_hit:
        if (x, y) == ship_to_hit:
            other_board.board[x][y] = '#'
            print('you sank my battleship')
        else:
            board.guesses.append((x, y))
            other_board.board[x][y] = 'X'

    print('You missed this time')


def new_game():
    """
    Runs main game every time user reloads
    or restarts the game
    """
    print('~' * 60)
    print('WELCOME TO BATTLESHIPS')
    print('~' * 60)
    name = input('Please enter your name here:\n')
    print(f"Hi {name}. Some rules before we start...\n")
    data = get_user_data()
    size = int(data[0])
    num_of_ships = int(data[1])

    print('Creating new game...\n')

    player_board = Board(name, size, num_of_ships, type='player')
    computer_board = Board('computer', size, num_of_ships, type='computer')

    populate_game_board(player_board)
    print('~' * 60)
    populate_game_board(computer_board)

    player_guess = make_guess(player_board)
    comp_guess = make_guess(computer_board)
    row = player_guess[0]
    col = player_guess[1]
    validate_guess(player_board, computer_board, row, col)

    print('Finished Game')


new_game()