from units_lib import Player, knight
from framefunc import pause
from func import battle


def old_ruins(player: Player):
    while True:
        print("=" * 45)
        print("OLD RUINS")
        print("=" * 45)

        if "Past glory" not in player.quests:

            print("0. Leave old ruins")

            choice = input("Choose: ")

            if choice == "0":
                break

        elif "Past glory" in player.quests:

            print("0. Leave old ruins")
            print("1. Look for the knight's statue")

            choice = input("Choose: ")

            if choice == "0":
                break

            if choice == "1":
                print("You find a statue. It is holding a sword.")
                choice2 = input(
                    "Take the sword? (yes/no): "
                ).lower()
                if choice2 == "yes":
                    victory = battle(knight, player)
                    if victory:
                        print("You obtained the Sword of Dawn!")
                        player.artifacts.append("Sword of Dawn")
                        player.quests.remove("Past glory")
                        player.completed_quests.append("Past glory")
                        pause()
                    else:
                        break
                elif choice2 == "no":
                    print("You left the sword behind")
                else:
                    print("Invalid choice.")
                    continue


        elif "Past glory" in player.completed_quests:

            print("0. Leave old ruins")

            choice = input("Choose: ")

            if choice == "0":
                break
