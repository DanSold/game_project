from units_lib import Player
from framefunc import pause, mission_complete, mission_append

import time



def bridge(player: Player):
    while True:
        print("=" * 45)
        print("BRIDGE")
        print("=" * 45)

        if "One Wish" in player.completed_quests and "Charity" not in player.completed_quests:
            print("***You see a beggar on the bridge***")
            time.sleep(3)
            mission_append(player, "Charity")
            time.sleep(3)
            while True:
                choice = input("Give him 15 gold? (yes/no): ").lower()
                if choice == "yes":
                    if player.gold >= 15:
                        player.gold -= 15
                        print(f"-15 gold. Your gold now is {player.gold}")
                        time.sleep(3)
                        player.reputation += 15
                        print(f"+15 reputation. Your reputation is {player.reputation}")
                        time.sleep(3)
                        mission_complete(player, "Charity")
                        pause()
                        break
                    else:
                        print("You don't have enough gold!")
                        time.sleep(2)
                        print("***You walk past***")
                        time.sleep(3)
                        pause()
                        break
                elif choice == "no":
                    print("***You walk past***")
                    time.sleep(3)
                    pause()
                    break
                else:
                    print("Invalid input")
                    continue
            break
        if "Charity" in player.completed_quests:
            print("***You are standing on the bridge***")
            time.sleep(3)
            break
        else:
            print("***This is still too far away for you***")
            pause()
            break
