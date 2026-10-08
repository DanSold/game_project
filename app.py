import time

from framefunc import load_game_by_name, save_game
from func import *

from units_lib import Player

from locations import village, bandit_camp, forest, lake, old_ruins



def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)

    player = None

    print("1. New game")
    print("2. Load saved game")
    start_choice = input("Choose option: ")

    if start_choice == "2":
        player = load_game_by_name()
    if player is None:
        print("Now the dragon is awakening.")
        print("Five ancient artifacts are the only things that can stop what is coming.")

        name = input("Enter your name: ")
        player = Player(name)
        print(f"Welcome, {player.name}!")
        time.sleep(2)

    while player.health > 0:

        print("=" * 45)
        print("MAIN MENU")
        print("=" * 45)

        print("1. Eldoria Village")
        print("2. Bandit Camp")
        print("3. Forest")
        print("4. Lake")
        print("5. Old Ruins")
        print("6. Check your parameters and stats")
        print("7. Check your inventory")
        print("8. Chek quests")
        print("0. Quit game")
        print("+. Save game")

        choice = input("Choose destination: ")

        if choice == "1":
            village(player)

        elif choice == "2":
            bandit_camp(player)

        elif choice == "3":
            forest(player)

        elif choice == "4":
            lake(player)

        elif choice == "5":
            old_ruins(player)

        elif choice == "6":
            chek_param(player)

        elif choice == "7":
            chek_inventory(player)

        elif choice == "8":
            chek_quests(player)

        elif choice == "0":
            print("Thank you for playing The Last Flame!")
            break
        elif choice == "+":
            save_game(player)

        else:
            print("Invalid choice.")
            pause()

    if player.health <= 0:
        print("=" * 45)
        print("GAME OVER")
        print("=" * 45)

        print(
            "Your journey has come to an end."
        )


if __name__ == "__main__":
    main()
