import time

from units_lib import Player, dragon
from framefunc import pause, mission_append, mission_complete
from func import battle




def dragon_lair(player: Player):
    while True:

        if "Frozen Secrets" in player.completed_quests:
            print("=" * 45)
            print("DRAGON'S LAIR")
            print("=" * 45)
            print("***The ambient heat is suffocating. Flames flicker along the ancient cavern walls.***")
            time.sleep(2.5)

            if "Dragon Slayer" in player.completed_quests or "True Hero" in player.completed_quests:
                print("0. Leave the Lair")
                print("***The fate of the dragon and Morvain has already been decided***")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "The Final Confrontation")
                time.sleep(2)
                print("0. Leave the Lair")
                print("1. Approach the Last Dragon")

                choice = input("Choose: ")

                if choice == "0":
                    return

                elif choice == "1":
                    print("\n*** A giant crimson dragon lands before you, its glowing eyes locking onto yours. ***")
                    time.sleep(3)


                    if player.reputation >= 30:
                        print(
                            "Dragon: 'Human... I see you've found all 5 artifacts. You know the truth.'")
                        time.sleep(3)
                        print(
                            "Dragon: 'Morvain manipulated us all to claim absolute power. Will you fight me, or face the true villain?'")
                        time.sleep(3)

                        print("\nWhat will you do?")
                        print("1. Speak with the Dragon")
                        print("2. Attack the Dragon regardless")

                        rep_choice = input("Choose: ")

                        if rep_choice == "1":
                            print(
                                "\n***The Dragon nods peacefully and breathes a warm, protective barrier over you***")
                            time.sleep(3)
                            print(
                                "Dragon: 'Go to the Sorcerer's Tower. Morvain awaits you at the summit. I grant you safe passage.'")
                            time.sleep(3)
                            player.quests_items.append("Dragon's Blessing")
                            mission_complete(player, "The Final Confrontation")
                            print(
                                "\n***The pathway to the Sorcerer's Tower is now unlocked in your main map!***")
                            pause()
                            return
                    print("\n***The Dragon roars as the battle begins!***")
                    time.sleep(2.5)
                    victory = battle(dragon, player)
                    if victory:
                        print("\n***The mighty dragon falls with a deafening crash...***")
                        time.sleep(3)
                        print("\nWhat will you do with the Dragon's Power?")
                        print("1. Claim the power for yourself")
                        print("2. Surrender the power to Morvain")

                        end_choice = input("Choose your destiny: ")

                        if end_choice == "1":
                            print(f"***{player.name} absorbs the essence of the Last Dragon***")
                            time.sleep(3)
                            print("You become the supreme ruler of Eldoria, feared by all.")
                            print("=== NEUTRAL ENDING: THE NEW OVERLORD ===")
                            mission_complete(player, "The Final Confrontation")
                            pause()
                            return

                        elif end_choice == "2":
                            print(f"\n*** {player.name} hands the dragon's soul to Morvain. ***")
                            time.sleep(3)
                            print("Morvain laughs maniacally as darkness consumes the realm.")
                            print("=== BAD ENDING: MORVAIN'S TRIUMPH ===")
                            mission_complete(player, "The Final Confrontation")
                            pause()
                            return
                        else:
                            print("Invalid choice.")
                    else:
                        print("The dragon's fire forced you to retreat...")
                        pause()
                        return
                else:
                    print("Invalid choice.")
        else:
            print("***This is still too far away for you***")
            pause()
            return