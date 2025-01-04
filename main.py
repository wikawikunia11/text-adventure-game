import sys
from clear_console import clear_terminal
from time import sleep
from player import Player
from world import World


def main():
    clear_terminal()

    print("Welcome to the Game!")

    while True:
        print("\nMain Menu:")
        print("1. Start Game")  # co z zapisaną grą
        print("2. Exit")

        choice = input("Enter a number of your choice: ")

        if choice == "1":
            print("Starting the game...")
            start_game("loactions.json", "player.json")

        elif choice == "2":
            print("Exiting the game. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


def get_game_description():
    with open("game_start.txt", 'r') as file:
        print(file.read())


def start_game(world_file, player_file):
    clear_terminal()
    get_game_description()
    sleep(20)
    World(world_file)
    Player(player_file)


if __name__ == "__main__":
    main()
