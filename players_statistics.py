from MODULES.get_statistics import get_game_statistics


def get_all_players():
    game_statistics = get_game_statistics()

    players_lst = []

    for stat in game_statistics:
        player_1 = stat["PLAYER 1"]
        player_2 = stat["PLAYER 2"]

        players_lst.extend([player_1, player_2])

    return sorted(set(players_lst))


def update_player_stats(player_name: str, stat_line: dict, player_stat: dict) -> None:
    players_lst = [stat_line["PLAYER 1"], stat_line["PLAYER 2"]]

    win = int(stat_line["WIN"])
    draw = int(stat_line["DRAW"])
    loose = int(stat_line["LOOSE"])

    if player_name in players_lst:
        if player_name == players_lst[0]:
            player_stat[player_name]["WIN"] += win
            player_stat[player_name]["LOOSE"] += loose
        else:
            player_stat[player_name]["LOOSE"] += win
            player_stat[player_name]["WIN"] += loose

        player_stat[player_name]["DRAW"] += draw


def get_text_line(player_name: dict) -> str:
    player_stat = {player_name: {"WIN": 0, "DRAW": 0, "LOOSE": 0}}

    for stat in get_game_statistics():
        update_player_stats(player_name, stat, player_stat)

    player_description = player_stat[player_name]
    line = " - ".join([f"{res}: {count}" for res, count in player_description.items()])

    return f"{player_name} - {line}"


def show_statistics():
    for player in get_all_players():
        print(get_text_line(player))

# show_statistics()