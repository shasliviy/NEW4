from MODULES.get_statistics import get_game_statistics


def get_winner(stat: dict, player1: str, player2: str) -> str:
    if stat["WIN"] == "1":
        return f"{player1} wins"
    elif stat["LOOSE"] == "1":
        return f"{player2} wins"
    else:
        return "DRAW"


def get_text_line(stat: dict) -> str:
    game_number = stat["GAME #"]
    player_1 = stat["PLAYER 1"]
    player_2 = stat["PLAYER 2"]
    game_date = stat["DATE"]

    winner = get_winner(stat, player_1, player_2)

    return f"{game_number} {player_1} : {player_2} - {game_date} - {winner}"


def show_first_line(number: int) -> str:
    if number >= 10:
        return (f"{number} games were played.\n"
                "There are results of last 10 games:"), 10
    else:
        return (f"Only {number} games were played.\n"
                "There are results of the games:"), number


def show_last_results() -> None:
    statistics = get_game_statistics()
    games_played = len(statistics)
    info_message, games_to_show = show_first_line(games_played)
    print(info_message)

    last_results = statistics[-games_to_show:]

    for stat_dict in last_results:
        line = get_text_line(stat_dict)

        print(line)

# show_last_results()