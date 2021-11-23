import csv

def get_game_statistics(file = "output.csv") -> list:

    game_statistics = []

    with open(file, "r") as input_file:
        input_file_csv_dict = csv.DictReader(input_file, delimiter="|")
        for line in input_file_csv_dict:
            game_statistics.append(line)

    return game_statistics