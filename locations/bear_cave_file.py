import time

from units_lib import Player, bear_spirit, guardian_squad
from framefunc import pause, mission_append, mission_complete
from func import battle




def bear_cave(player: Player):
    while True:

        if "Flame Trial" in player.completed_quests:
            print("=" * 45)
            print("BEAR CAVE")
            print("=" * 45)
            print("***Damp earth and heavy stillness fill the cavern. Massive claws have scarred the stone walls.***")
            time.sleep(2.5)

            if "Bear Spirit Trial" in player.completed_quests:
                print("0. Leave the Cave")
                print("***The cave is silent. The spirit is no longer here***")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "Bear Spirit Trial")
                time.sleep(2)
                print("0. Leave the Cave")
                print("1. Enter the deep lair")

                choice = input("Choose: ")

                if choice == "0":
                    return

                elif choice == "1":
                    print("\n*** A colossal spectral bear steps out from the shadows, eyes burning with pale light. ***")
                    time.sleep(3)
                    print("Bear Spirit: 'Wanderer... You carry the warmth of the Eternal Fire.'")
                    time.sleep(3)
                    print("Bear Spirit: 'Lord Morvain builds a sanctuary to protect this realm from chaos.'")
                    time.sleep(3.5)
                    print("Bear Spirit: 'A group of Dragon Slayers Guild warriors lurks nearby, threatening our peace.'")
                    time.sleep(3.5)
                    print("Bear Spirit: 'Destroy the Guild squad to protect the sanctuary, and I shall reward you with gold.'")
                    time.sleep(4)

                    while True:
                        print("\n" + "-" * 45)
                        print("1. Protect the sanctuary: Kill the Guild squad")
                        print("2. Refuse the offer and walk away")
                        print("3. Attack and kill the Bear Spirit")
                        print("-" * 45)

                        choice_trial = input("Choose your decision: ")


                        if choice_trial == "1":
                            print("\n*** You track down and destroy the Guild squad for the promised reward... ***")
                            time.sleep(3)
                            victory = battle(guardian_squad, player)
                            if victory:
                                time.sleep(3)
                                print("Bear Spirit: 'You have served the sanctuary well. Take your gold.'")
                                time.sleep(3)
                                player.reputation -= 15
                                player.gold += 100
                                print(f"***You gained 100 Gold!***")
                                print(f"***Your reputation decreased dramatically (-15)! Current reputation: {player.reputation}***")
                                mission_complete(player, "Bear Spirit Trial")
                                pause()
                                return
                            else:
                                print("You were defeated and forced to retreat from the cave...")
                                pause()
                                return


                        elif choice_trial == "2":
                            print("\n*** You refuse to strike down the Guild warriors without reason. ***")
                            time.sleep(3)
                            print(f"{player.name}: 'I will not shed the blood of the Guild on your command.'")
                            time.sleep(3)
                            print("Bear Spirit: 'Then leave my cave before I lose my patience.'")
                            time.sleep(3)
                            print("[!] Reputation unchanged.")
                            mission_complete(player, "Bear Spirit Trial")
                            pause()
                            return

                        elif choice_trial == "3":
                            print("\n*** You draw your weapon to destroy the corrupting entity! ***")
                            time.sleep(2.5)

                            victory = battle(bear_spirit, player)
                            if victory:
                                print("\n*** The Bear Spirit collapses into pure white light and dissolves! ***")
                                time.sleep(3)
                                player.reputation += 15
                                print(f"***Your reputation increased significantly (+15)! Current reputation: {player.reputation}***")
                                time.sleep(3)
                                mission_complete(player, "Bear Spirit Trial")
                                pause()
                                return
                            else:
                                print("You were defeated and forced to retreat from the cave...")
                                pause()
                                return
                        else:
                            print("Invalid choice.")
        else:
            print("***This is still too far away for you***")
            pause()
            return
