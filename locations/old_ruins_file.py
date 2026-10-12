import time

from units_lib import Player, knight
from framefunc import pause, mission_append, mission_complete
from func import battle


def old_ruins(player: Player):
    while True:
        if "Eye of Truth" in player.artifacts:
            print("=" * 45)
            print("OLD RUINS")
            print("=" * 45)
            print("***There are ruins of an old castle all around***")
            time.sleep(3)

            if "Past glory" in player.completed_quests:
                print("0. Leave old ruins")
                choice = input("Choose: ")
                if choice == "0":
                    return

            else:
                mission_append(player, "Past glory")
                time.sleep(3)

                while True:
                    print("0. Leave old ruins")
                    print("1. Look for the knight's statue")
                    choice = input("Choose: ")

                    if choice == "0":
                        return

                    elif choice == "1":
                        print("You find a statue. It is holding a sword.")

                        while True:
                            choice2 = input("Take the sword? (yes/no): ").lower()

                            if choice2 == "yes":
                                time.sleep(3)
                                print("***The statue comes to life***")
                                time.sleep(3)
                                print("Knight: After so many years of sleep, I am alive again.")
                                time.sleep(3.5)
                                print("But the curse remains...")
                                time.sleep(3)

                                while True:
                                    print("-" * 15)
                                    print("1. Why were you cursed?")
                                    print("2. Who cursed you?")
                                    print("-" * 15)
                                    choice_replica = input("Choose a replica: ")

                                    if choice_replica == "1":
                                        print(f"{player.name}: Why were you cursed?")
                                        time.sleep(3)
                                        print("Knight: I did not obey them...")
                                        time.sleep(3)
                                        print(f"{player.name}: Whom?")
                                        time.sleep(2)
                                        break
                                    elif choice_replica == "2":
                                        print(f"{player.name}: Who cursed you?")
                                        break
                                    else:
                                        print("Invalid choice.")

                                print("Knight: Morv....")
                                time.sleep(1.2)
                                print("***The curse grows stronger, and the knight loses control...***")
                                time.sleep(2.5)

                                victory = battle(knight, player)
                                if victory:
                                    print("You obtained the Sword of Dawn!")
                                    player.artifacts.append("Sword of Dawn")
                                    mission_complete(player, "Past glory")
                                    pause()

                                return

                            elif choice2 == "no":
                                print("You left the sword behind")
                                break

                            else:
                                print("Invalid choice.")

                    else:
                        print("Invalid choice.")
        else:
            print("***This is still too far away for you***")
            pause()
            return