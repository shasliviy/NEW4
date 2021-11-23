# Запустить цикл на 100 000 итераций с возможными исходами вводовв и имен по рандому

import time
import random as ra
from MODULES.write_to_file import write_results_to_file


def get_list_of_players(file="GOT_Characters.txt") -> list:
    list_players = []

    with open(file, "r") as input_file:
        for line in input_file:
            list_players.append(line.rstrip())

    return list_players


def get_pair_of_players() -> dict:
    list_of_players = get_list_of_players()

    player_1_name = ra.choice(list_of_players)
    list_of_players.remove(player_1_name)
    player_2_name = ra.choice(list_of_players)

    players_names = {"PLAYER 1": player_1_name, "PLAYER 2": player_2_name}

    return players_names


def get_random_results() -> str:
    final_status = ["DRAW", "X", "O"]
    result = ra.choice(final_status)

    return result


def create_db() -> None:
    status = get_random_results()
    players = get_pair_of_players()

    write_results_to_file(status_game=status, players_names=players)


def make_records_to_db(number=50):
    for _ in range(number):
        create_db()
        time.sleep(13.5)


make_records_to_db(1000)