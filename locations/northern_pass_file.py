import time

from units_lib import Player, ice_golem
from framefunc import pause, mission_append, mission_complete
from func import battle




def northern_pass(player: Player):
    while True:

        if "Flame Trial" in player.completed_quests:
            print("=" * 45)
            print("NORTHERN MOUNTAIN PASS")
            print("=" * 45)
            print("***Bitter cold winds whip around the jagged, snow-covered cliffs.***")
            time.sleep(2.5)

            if "Soul Crystal" in player.artifacts:
                print("0. Leave the Northern Pass")
                print("The pass is quiet, swept by endless blizzards.")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "Frozen Secrets")
                time.sleep(2)
                print("0. Leave the Northern Pass")
                print("1. Climb towards the Ancient Ice Shrine")

                choice = input("Choose: ")

                if choice == "0":
                    return

                elif choice == "1":
                    print("\n*** You push through the blinding snow towards the shrine. ***")
                    time.sleep(2.5)
                    print("A massive Ice Golem steps out from the blizzard, guarding the path!")
                    time.sleep(2.5)

                    victory = battle(ice_golem, player)
                    if victory:
                        print("\n*** The Ice Golem shatters into thousands of frozen shards! ***")
                        time.sleep(3)
                        print("At the altar, you claim the legendary Soul Crystal!")
                        time.sleep(3)

                        player.artifacts.append("Soul Crystal")
                        mission_complete(player, "Frozen Secrets")

                        if player.reputation >= 30:
                            print(f"\n*** As {player.name} holds the Soul Crystal, a glowing vision appears! ***")
                            time.sleep(3.5)
                            print("You see the ancient wizard Morvain orchestrating the war from the shadows.")
                            time.sleep(4)
                            print("You now know the truth about Morvain's deception!")
                            time.sleep(4)
                        else:
                            print("\nYou hold the cold crystal, feeling its power ready for the final battles.")
                            time.sleep(3)

                        pause()
                        return
                    else:
                        print("The icy cold forces you to retreat...")
                        pause()
                        return
                else:
                    print("Invalid choice.")
        else:
            print("***This is still too far away for you***")
            pause()
            return