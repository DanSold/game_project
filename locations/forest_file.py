from units_lib import Player, werewolf
from framefunc import mission_complete, pause
from func import battle

import time


def forest(player: Player):
    def give_eye_of_truth():
        if "Eye of Truth" not in player.artifacts:
            player.artifacts.append("Eye of Truth")
            print("+ Eye of Truth")
            print("The shaman gave you the Eye of Truth.")
            time.sleep(3)

        if "Orb of Wishes" in player.quests_items:
            player.quests_items.remove("Orb of Wishes")

        if "One Wish" in player.quests:
            mission_complete(player, "One Wish")

        pause()

    def steal_eye_of_truth():
        if "Eye of Truth" not in player.artifacts:
            player.artifacts.append("Eye of Truth")

        print("+ Eye of Truth")
        time.sleep(3)
        mission_complete(player, "One Wish")
        time.sleep(3)

        player.reputation -= 10
        print(
            f"Reputation -10 | "
            f"Your reputation -> {player.reputation}"
        )

        player.health -= 20
        print(
            f"You got a curse -20 HP | "
            f"Your health -> {player.health}"
        )

        pause()

    def search_hut():
        print("***You found the Eye of Truth***")

        choice = input(
            "Do you want to pick it up? (yes/no): "
        ).lower()

        if choice == "yes":
            steal_eye_of_truth()

        elif choice == "no":
            print("***You left the Eye of Truth***")
            pause()

        else:
            print("Invalid choice.")

    def enter_hut(first_visit: bool):

        if first_visit:
            print("***There is a werewolf in the hut***")
            time.sleep(4)

            victory = battle(werewolf, player)

            if not victory:
                return False

            else:
                print("Werewolf died.")
                pause()

                print(f"***{player.name} walks up to the shaman***")
                time.sleep(4)

                print("***The shaman is badly wounded***")
                time.sleep(3)

                print(
                    "Shaman: Go to the lake and catch the magic fish."
                    "\nIt will grant you any wish..."
                    "\nSave my life..."
                )

                time.sleep(4)

                mission_complete(player, "Old Stories")
                time.sleep(4)

                if "One Wish" not in player.quests:
                    player.quests.append("One Wish")

                print("\nYou got a new quest!")
                print("=== One Wish ===")
                pause()

        else:
            while True:
                if "Orb of Wishes" in player.quests_items:
                    print("0. Leave hut")
                    print("1. Search the hut")
                    print("2. Save the Shaman")
                    choice = input("Choose: ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        search_hut()
                        if "Eye of Truth" in player.artifacts:
                            break
                    elif choice == "2":
                        give_eye_of_truth()
                    else:
                        print("Invalid choice.")
                else:
                    print("0. Leave hut")
                    print("1. Search the hut")
                    choice = input("Choose: ")
                    if choice == "0":
                        break
                    elif choice == "1":
                        search_hut()
                        if "Eye of Truth" in player.artifacts:
                            break
                    else:
                        print("Invalid choice.")
            return True

    while True:
        print("=" * 45)
        print("FOREST")
        print("=" * 45)

        if (
                "Old Stories" in player.quests
                and "One Wish" not in player.quests
        ):
            print("***Dark forest is around***")
            time.sleep(4)

            print("0. Leave forest")
            print("1. Enter the shaman's hut")

            choice = input("Choose: ")

            if choice == "0":
                break

            elif choice == "1":
                enter_hut(first_visit=True)

                if player.health <= 0:
                    return

            else:
                print("Invalid choice.")


        elif (
                "Old Stories" in player.completed_quests
                and "One Wish" in player.quests
        ):
            print("0. Leave forest")
            print("1. Enter the shaman's hut")

            choice = input("Choose: ")

            if choice == "0":
                break

            elif choice == "1":
                enter_hut(first_visit=False)

            else:
                print("Invalid choice.")

        else:
            print("***Dark forest is around***")
            time.sleep(4)
            break
