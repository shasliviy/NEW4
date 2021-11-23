import datetime as dt
import csv


# from pprint import pprint


def get_date() -> str:
    date_format = '%d.%m.%Y %H:%M:%S'
    now = dt.datetime.now()
    return now.strftime(date_format)


def get_game_number(file="output.csv") -> str:
    with open(file, "r") as input_file:
        input_file_csv_dict = csv.DictReader(input_file, delimiter="|")
        return str(len(list((input_file_csv_dict))) + 1)


def get_result_dic(status_game: str) -> dict:
    results = {'WIN': 0,
               'DRAW': 0,
               'LOOSE': 0
               }

    if status_game == "X":
        results["WIN"] = 1
    elif status_game == "O":
        results["LOOSE"] = 1
    elif status_game == "DRAW":
        results["DRAW"] = 1

    return results


def get_final_dict(some_file: str, status_game: str, players: dict) -> dict:
    game_number = get_game_number(some_file)
    result_dict = {"GAME #": game_number}
    result_dict.update(players)
    result_dict.update(get_result_dic(status_game))

    now = get_date()
    result_dict["DATE"] = now

    return result_dict


def write_results_to_file(status_game: str, players_names: dict, file="output.csv") -> None:
    results = get_final_dict(file, status_game, players_names)
    fields = results.keys()

    with open(file, "a+", newline="") as output_csv:
        output_writer = csv.DictWriter(output_csv, fieldnames = fields, delimiter="|")
        output_writer.writerow(results)

        print("RESULTS ADDED TO FILE")
