from func import pause, chek_inventory, chek_quests, chek_param
from units_lib import Player
from locations import village, bandit_camp, old_ruins


def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)
    print("Now the dragon is awakening.")
    print("Five ancient artifacts are the only things that can stop what is coming.")

    name = input("Enter your name: ")
    player = Player(name)
    print(f"Welcome, {player.name}!")

    while player.health > 0:

        print("=" * 45)
        print("MAIN MENU")
        print("=" * 45)

        print("1. Visit Eldoria Village")
        print("2. Visit Bandit Camp")
        print("3. Old Ruins")
        print("4. Check your parameters and stats")
        print("5. Check your inventory")
        print("6. Chek quests")
        print("0. Quit game")

        choice = input("Choose destination: ")

        if choice == "1":
            village(player)

        elif choice == "2":
            bandit_camp(player)

        elif choice == "3":
            old_ruins(player)

        elif choice == "4":
            chek_param(player)

        elif choice == "5":
            chek_inventory(player)

        elif choice == "6":
            chek_quests(player)

        elif choice == "0":
            print("Thank you for playing The Last Flame!")
            break

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
