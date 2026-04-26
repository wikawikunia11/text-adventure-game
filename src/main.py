import sys
from src.utils.clear_console import clear_terminal
from src.models.player import Player
from time import sleep
from src.models.world import World


def main():
    clear_terminal()

    print("Welcome to the Game!")

    while True:
        clear_terminal()
        print("\nMain Menu:")
        print("1. Start New Game")
        print("2. Continue saved game")
        print("3. Exit")

        choice = input("Enter a number of your choice: ")

        if choice == "1":
            clear_terminal()
            print("Starting the game...")
            sleep(2)
            start_game("src/data/locations.json", "src/data/player.json")
        elif choice == "2":
            clear_terminal()
            print("Starting saved game...")
            sleep(2)
            start_game("src/data/saved_game.json", "src/data/saved_player.json")
        elif choice == "3":
            clear_terminal()
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            clear_terminal()
            print("Invalid choice. Please try again.")
            sleep(2)


def get_game_description():
    with open("src/data/game_start.txt", 'r') as file:
        print(file.read())
        print("1. Continue")
        print("2. Exit")
        choice = input("Enter a number of your choice: ")
        if choice == "1":
            return
        elif choice == "2":
            clear_terminal()
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            clear_terminal()
            print("Invalid choice. Please try again.")
            sleep(2)
            get_game_description()


def start_game(world_file, player_file):
    clear_terminal()
    get_game_description()
    world = World(world_file)
    player = Player(player_file)
    clear_terminal()
    loc = player.find_location(player.location, world.location_list)
    player.decision(loc, world)


if __name__ == "__main__":
    main()
