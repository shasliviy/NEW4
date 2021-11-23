from MODULES.write_to_file import write_results_to_file


def valid_name(name: str) -> bool:
    if len(name) >= 3:
        contains_digit = not (name.isalpha())

        if contains_digit:
            if name.isdigit():
                return True
            else:
                return False

        else:

            lower_case_name = name.lower()
            upper_case_name = name.upper()

            if name == lower_case_name or name == upper_case_name:
                return True

    return False


def create_players_names() -> dict:
    players_names = {"PLAYER 1": "", "PLAYER 2": ""}

    for i in range(1, 3):
        status = False
        while not status:
            player_name = input(f"Enter Player's #{i} name: ")
            if valid_name(player_name):
                players_names[f"PLAYER {i}"] = player_name
                status = True
            else:
                continue

    return players_names


def generate_cells() -> list:
    space = "_"
    board = []

    for _ in range(3):
        temp_lst = []
        for _ in range(3):
            temp_lst.append(space)
        board.append(temp_lst)

    return board


def print_board(board: list) -> None:
    print("---------")
    for row in board:
        line = " ".join(row)
        print(f"| {line} |")
    print("---------")


def get_winner(board: list) -> str:
    # Проверка всех 3х символов в строчке
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] != "_":
            return f"{board[row][0]}"

    # Проверка всех 3х символов в столбике
    for column in range(0, 3):
        if board[0][column] == board[1][column] == board[2][column] != "_":
            return f"{board[0][column]}"

    # Проверка всех 3х символов по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return f"{board[1][1]}"

    if board[0][2] == board[1][1] == board[2][0] != "_":
        return f"{board[1][1]}"

    return False


def get_coord(line: str) -> tuple:
    x, y = line.strip().split()
    return int(x), int(y)


def coords_to_row_col(x: int, y: int) -> tuple:
    row = x - 1
    column = y - 1
    return row, column


def valid_сoordinates(board: list, coordinates: str) -> bool:
    try:
        coord_x, coord_y = get_coord(coordinates)
    except Exception:
        print("You must enter numbers")
        return False

    if not (1 <= coord_x <= 3 and 1 <= coord_y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False

    row, column = coords_to_row_col(coord_x, coord_y)

    if board[row][column] != "_":
        print("The cell is already occupied!")
        return False

    return True


def make_move(board: list, x: int, y: int, symbol: str) -> None:
    row, column = coords_to_row_col(x, y)
    board[row][column] = symbol


def game_status(game) -> str:
    winner = get_winner(game)

    if winner:
        return winner

    if "_" in game[0] or "_" in game[1] or "_" in game[2]:
        return "Game not finished"
    else:
        return "DRAW"


def get_current_player(players: dict, player_number: int) -> str:
    return players[f"PLAYER {player_number + 1}"]


def get_congratulations_line(status_game: str, players_names: dict):
    symbols = ["X", "O"]

    if status_game in symbols:
        player_number = symbols.index(status_game)
        winner = players_names[f"PLAYER {player_number + 1}"]
        return f"{winner} wins"
    else:
        return "DRAW"


def play_game() -> None:
    board = generate_cells()

    players = create_players_names()
    status = "playing"
    play_round = 1
    symbols = ["X", "O"]
    final_status = ["DRAW", "X", "O"]

    print_board(board)

    while status not in final_status:
        play_round = play_round + 1
        player_number = play_round % 2
        symbol = symbols[player_number]
        current_player = get_current_player(players, player_number)

        print(f"PLAYER {player_number + 1}, your turn!")

        coords = input(f"{current_player}, enter the coordinates: > ")

        while not valid_сoordinates(board, coords):
            coords = input(f"{current_player}, enter the coordinates: > ")

        coord_x, coord_y = get_coord(coords)
        make_move(board, coord_x, coord_y, symbol)
        print_board(board)
        status = game_status(board)

    congratulations_line = get_congratulations_line(status, players)
    print()
    print(congratulations_line)
    write_results_to_file(status_game=status, players_names=players)

# play_game()