import time

from units_lib import Player, morvain
from framefunc import pause, mission_append, mission_complete
from func import battle


def sorcerer_tower(player: Player):
    while True:
        if "Dragon's Blessing" in player.quests_items:
            print("=" * 45)
            print("SORCERER'S TOWER")
            print("=" * 45)
            print("***Dark storm clouds circle the spire where Morvain gathers his dark energy.***")
            time.sleep(2.5)

            if "True Hero" in player.completed_quests:
                print("0. Leave the Tower")
                print("Morvain has been defeated. Eldoria is at peace.")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "True Hero")
                time.sleep(2)
                print("0. Leave the Tower")
                print("1. Ascend to the top chamber and confront Morvain")

                choice = input("Choose: ")

                if choice == "0":
                    return

                elif choice == "1":
                    print("\n*** You burst into the dark chamber. Morvain turns, shocked to see you alive! ***")
                    time.sleep(3)
                    print("Morvain: 'Impossible! The Dragon should have destroyed you!'")
                    time.sleep(3)
                    print(f"{player.name}: 'Your deceit ends today, Morvain!'")
                    time.sleep(3)

                    victory = battle(morvain, player)
                    if victory:
                        print("\n*** Morvain screams as his magical core shatters into dust! ***")
                        time.sleep(3)
                        print("With Morvain destroyed, the dark spell breaks.")
                        print("The Last Dragon soars through the sky, now a protector of the realm.")
                        print("=== GOOD / TRUE ENDING: SAVIOR OF ELDORIA ===")
                        mission_complete(player, "True Hero")
                        pause()
                        return
                    else:
                        print("Morvain's dark magic crushed your spirit...")
                        pause()
                        return
                else:
                    print("Invalid choice.")
        else:
            print(
                "***This is still too far away for you***")
            pause()
            return
