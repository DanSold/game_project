import time

from units_lib import Player
from framefunc import pause, mission_append, mission_complete



def dragon_slayers_guild(player: Player):
    while True:
        if "Charity" in player.quests or "Charity" in player.completed_quests:
            print("=" * 45)
            print("Dragon Slayers' Guild")
            print("=" * 45)
            print("***Before you stands the majestic castle of the Dragon-Slayers' Guild.***")
            time.sleep(3)
            if "Heroes of the Past" in player.completed_quests:
                print("0. Leave the castle")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "Heroes of the Past")
                print("0. Leave the castle")
                print("1. Enter the Vault (Solve the Elemental Puzzle)")
                choice = input("Choose: ")
                if choice == "0":
                    return
                elif choice == "1":
                    print("\nYou see an altar with 5 elemental slots: Fire, Water, Earth, Air, Light.")
                    time.sleep(3)
                    print(
                        "Hint on the wall: 'Earth gives birth to Air, Light clears the sky, Fire follows, and Water washes all.'")

                    # key -> ["earth", "air", "light", "fire", "water"]
                    sequence = []
                    elements = {"1": "earth", "2": "air", "3": "light", "4": "fire", "5": "water"}

                    while len(sequence) < 5:
                        print("\nChoose next element:")
                        print("1. Earth | 2. Air | 3. Light | 4. Fire | 5. Water")
                        elem_choice = input("Select element (or 0 to reset): ")

                        if elem_choice == "0":
                            sequence.clear()
                            print("Puzzle reset.")
                            break
                        elif elem_choice in elements:
                            sequence.append(elements[elem_choice])
                            print(f"Current sequence: {' -> '.join(sequence)}")
                        else:
                            print("Invalid choice.")

                    if sequence == ["earth", "air", "light", "fire", "water"]:
                        print("\n*** The vault doors heavy slide open! ***")
                        time.sleep(3)
                        print("You found one of the Ancient Artifacts!")
                        time.sleep(3)
                        print("You obtained the Dragon Shield!")
                        player.artifacts.append("Dragon Shield")
                        time.sleep(3)
                        if player.reputation >= 15:
                            print(f"***As soon as {player.name} touches the artifact, the world around him disappears.***")
                            time.sleep(4)
                            print(
                                "***He finds himself in an ancient temple. A mage named Morvain stands before a massive stone door.***")
                            time.sleep(5)
                            print("Morvain: For thousands of years, you have hidden this power from us.")
                            time.sleep(3)
                            print("But soon, it will be mine!")
                            time.sleep(4)

                            print(
                                f"***The vision changes. {player.name} sees human cities burning, dead dragons, and armies fighting each other.***")
                            time.sleep(5)
                            print(
                                "***Morvain secretly manipulates both sides, fueling their hatred to achieve his own goal.***")
                            time.sleep(5)

                            print("A mysterious voice: He sowed hatred between humans and dragons to destroy their protectors")
                            print("and claim the power they had guarded for thousands of years.")
                            time.sleep(6)

                            print(f"***{player.name} sees Morvain standing before the stone door again, but it remains sealed.***")
                            time.sleep(4)
                            print("Morvain: Where are you hiding, you wretched beast?")
                            time.sleep(3)
                            print("You are the only thing standing between me and my destiny!")
                            time.sleep(4)
                            print("***Morvain strikes the stone door in rage.***")
                            time.sleep(3)

                            print("A mysterious voice: All the dragons have perished...")
                            time.sleep(3)
                            print("...except one.")
                            time.sleep(3)
                            print("The last guardian has disappeared, and even Morvain has failed to find him.")
                            time.sleep(5)
                            print("As long as the dragon lives, the power will remain beyond Morvain's reach.")
                            time.sleep(5)

                            print("***The vision fades, and Den returns to reality.***")
                            time.sleep(4)
                            print(
                                "***He now knows that the war between humans and dragons was orchestrated by a single mage.***")
                            time.sleep(5)
                            print("***And somewhere in this world, the last dragon is still alive...***")
                            time.sleep(4)
                            print("***The only one who can stop Morvain.***")
                            time.sleep(4)
                        else:
                            print("***You take the shield, feeling its ancient power pulsing in your hands.***")
                            time.sleep(3)
                        mission_complete(player, "Heroes of the Past")
                        pause()
                        break
                    elif len(sequence) == 5:
                        print("\n*** Wrong combination! Flames burst from the walls! ***")
                        player.health -= 15
                        print(f"-15 HP! Your health is now {player.health}")
                        pause()

        else:
            print("***This is still too far away for you***")
            pause()
            return
