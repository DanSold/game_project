from units_lib import Player


def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)

    print("Now the dragon is awakening.")
    print("Five ancient artifacts are the only things " "that can stop what is coming.")
    name = input("Enter your name: ")
    player = Player(name)
    print(f"Welcome, {player.name}!")


if __name__ == "__main__":
    main()
