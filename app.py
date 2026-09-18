from units_lib import Player
from locations import village

def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)
    print("Now the dragon is awakening.")
    print("Five ancient artifacts are the only things " "that can stop what is coming.")

    name = input("Enter your name: ")
    player = Player(name)
    print(f"Welcome, {player.name}!")

    while player.health > 0:

        print("\n" + "=" * 45)
        print("MAIN MENU")
        print("=" * 45)

        print("1. Visit Eldoria Village")
        print("0. Quit game")

        choice = input("Choose destination: ")
        if choice == "1":
            village()
        elif choice == "0":
            print("Thank you for playing The Last Flame!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
