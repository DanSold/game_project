from framefunc import load_game_by_name, save_game
from func import *

from units_lib import Player

from locations import village, bandit_camp, forest, lake, old_ruins, bridge, dragon_slayers_guild, temple_of_fire, \
    dead_forest, bear_cave, northern_pass, dragon_lair, sorcerer_tower


def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)

    player = None

    print("1. New game")
    print("2. Load saved game")
    start_choice = input("Choose option: ")

    if start_choice == "1":
        print("Now the dragon is awakening.")
        print("Five ancient artifacts are the only things that can stop what is coming.")

        name = input("Enter your name: ")

        if not name:
            print("Name cannot be empty.")

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
        print("5. Bridge")
        print("6. Dragon Slayers' Guild")
        print("7. Old Ruins")
        print("8. Dead Forest")
        print("9. Temple of Fire")
        print("10. Bear Cave")
        print("11. Northern Mountain Pass")
        print("12. Dragon's Lair")
        print("13. Sorcerer's Tower")
        print("14. Check your parameters and stats")
        print("15. Check your inventory")
        print("16. Chek quests")
        print("17. Quit game")
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
            bridge(player)

        elif choice == "6":
            dragon_slayers_guild(player)

        elif choice == "7":
            old_ruins(player)

        elif choice == "8":
            dead_forest(player)

        elif choice == "9":
            temple_of_fire(player)

        elif choice == "10":
            bear_cave(player)

        elif choice == "11":
            northern_pass(player)

        elif choice == "12":
            dragon_lair(player)

        elif choice == "13":
            sorcerer_tower(player)

        elif choice == "14":
            chek_param(player)

        elif choice == "15":
            chek_inventory(player)

        elif choice == "16":
            chek_quests(player)

        elif choice == "17":
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
