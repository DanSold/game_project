import time

from units_lib import Player, fire_guardian
from framefunc import pause, mission_append, mission_complete
from func import battle





def temple_of_fire(player: Player):
    while True:
        if "Heroes of the Past" in player.completed_quests and "Past glory" in player.completed_quests:
            print("=" * 45)
            print("TEMPLE OF FIRE")
            print("=" * 45)
            print("***You stand before massive obsidian gates radiating intense heat.***")
            time.sleep(3)

            if "Eternal Fire" in player.artifacts or "Flame Trial" in player.completed_quests:
                print("0. Leave the temple")
                print("The temple is quiet. The sacred flame burns peacefully.")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "Flame Trial")
                time.sleep(3)
                print("0. Leave the temple")
                print("1. Approach the Altar of Eternal Fire")

                choice = input("Choose: ")

                if choice == "0":
                    return

                elif choice == "1":
                    print("\n***You step into the glowing sanctuary. In the center burns a blinding flame***")
                    time.sleep(3)
                    print("***As you get closer, the flames suddenly twist and form a towering figure!***")
                    time.sleep(3)
                    print("Fire Guardian: Only those who carry the light of dawn may claim the Eternal Fire...")
                    time.sleep(3)
                    if "Ash Blessing" in player.quests_items:
                        print(
                            "***The entity senses that a blessing has been placed upon you***")
                        time.sleep(3)
                        print(
                            "Fire Guardian: Ah... I sense the blessing of the lost spirits. You carry their quiet strength.")
                        time.sleep(3)
                        print("***The guardian bows its head, stepping aside without a fight***")
                        time.sleep(3)
                        print("***You approach the altar and take the pulsing core of flame***")
                        time.sleep(3)
                        print("You obtained the Eternal Fire!")
                        player.artifacts.append("Eternal Fire")
                        mission_complete(player, "Flame Trial")
                        pause()
                        return
                    else:
                        print("*** The Fire Guardian attacks! ***")
                        time.sleep(2.5)
                        victory = battle(fire_guardian, player)
                        if victory:
                            print("\n***The guardian dissolves into a harmless cascade of sparks***")
                            time.sleep(3)
                            print("You approach the altar and take the pulsing core of flame.")
                            time.sleep(3)
                            print("You obtained the Eternal Fire!")
                            player.artifacts.append("Eternal Fire")
                            mission_complete(player, "Flame Trial")
                            pause()
                            return
                        else:
                            print("You were scorched by the sacred flames and forced to retreat...")
                            pause()
                            return
                else:
                    print("Invalid choice.")
        else:
            print(
                "***This is still too far away for you***")
            pause()
            return
