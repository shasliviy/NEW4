from TicTacToe import play_game
from last_games import show_last_results
from players_statistics import show_statistics

def print_introduction() -> None:
    message = ("Hello, dear user!\n"
                "You can pick one of the following actions:\n"
                "1. 'play'       - Play TicTacToe with your friend.\n"
                "2. 'last-games' - Show statistics about last 10 games.\n"
                "3. 'statistics' - Show all players that have ever played the game.")
    print(message)


def process_command() -> None:
    cmd = input("Enter your command: ")

    if cmd == "play":
        play_game()
    elif cmd == "last-games":
        show_last_results()
    elif cmd == "statistics":
        show_statistics()


def main():
    print_introduction()
    process_command()


if __name__ == "__main__":
    main()

