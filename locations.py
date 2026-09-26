from func import pause, battle, open_shop, blacksmith
from units_lib import *
import time


def village(player: Player):
    while True:
        print("=" * 45)
        print("ELDORIA VILLAGE")
        print("=" * 45)

        print("0. Leave village")
        print("1. Talk to the Elder")
        print("2. Merchant")
        print("3. Shop")
        print("4. Blacksmith")

        choice = input("Choose: ")

        if choice == "0":
            break

        elif choice == "1":
            print("ELDER:")

            if "Old Stories" not in player.quests and "Old Stories" not in player.completed_quests:
                print("***The village elder tells the children a legend.***")
                time.sleep(2)
                print(
                    "For more than 1,000 years, humans and dragons have been at war."
                )
                time.sleep(3)
                print(
                    "For most of this conflict, humans lost "
                    "\nbut 150 years ago, the Dragon Slayers' Guild was founded."
                )
                time.sleep(6)
                print("This guild consisted of the bravest warriors and the most powerful mages.")
                time.sleep(4)
                print("Together, they created five artifacts that allowed them to defeat the dragons."
                      "\nToday, none of these warriors are still alive.")
                time.sleep(5)
                print("However, so much time has passed that there are almost no memories or stories left"
                      "\nabout the true cause of the war.")
                time.sleep(5)
                print("***Moreover, the village elder tells them about rumors that a dragon was recently spotted.***")
                time.sleep(4)
                print(f"***{player.name} walks over to the village elder.***")
                time.sleep(5)
                print(f"{player.name}: Is it really true?")
                time.sleep(2)
                print("Village Elder: What exactly?")
                time.sleep(2)
                print("A legend is just a legend. And as for that dragon... ")
                time.sleep(3)
                print("I don't know either. An old shaman came by recently. ")
                time.sleep(3)
                print("He said that he had seen a dragon at night. No one here believed him. ")
                time.sleep(3)
                print("He has been living alone in the forest for a long time... Maybe he has gone crazy by now.")
                time.sleep(3)
                print(f"{player.name}: In the forest, you say...")
                time.sleep(3)
                print("Village Elder: If you like listening to stories, you can visit him. "
                      "\nBut I have to get back to my business now...")

                player.quests.append("Old Stories")
                print("\nYou got a new quest!")
                print("=== Old Stories ===")
                pause()

            elif "Old Stories" in player.quests:
                print("Time flies....")
                pause()

            elif "Old Stories" in player.completed_quests:
                print(
                    "You survived, and that's good."
                )
                pause()

        elif choice == "2":

            print("Merchant: Ooo, you look like the kind of person I need...")
            time.sleep(3)
            print(f"{player.name}: Huh?")
            time.sleep(2)
            print("Merchant: Listen, I’ll pay you. "
                  "\nI’ve already asked everyone, but no one even wants to come there.")
            time.sleep(4)
            print(f"{player.name}: I don't understand you.")
            time.sleep(3)
            print("Merchant: Bandits robbed me and took my cart loaded with goods. "
                  "\nThey’re at their camp right now. Go and retrieve what belongs to me. ")
            time.sleep(6)
            print("I don’t care how you do it — whether you kill them all or simply sneak in and take it back. ")
            time.sleep(4)
            print("Just make sure you return my goods to me.")
            time.sleep(4)

            player.quests.append("Gold, gold, gold...")
            print("\nYou got a new quest!")
            print("=== Gold, gold, gold... ===")
            pause()


        elif choice == "3":
            open_shop(player)

        elif choice == "4":
            blacksmith(player)

        else:
            print("Invalid choice.")


def bandit_camp(player: Player):
    while True:
        print("=" * 45)
        print("BANDIT CAMP")
        print("=" * 45)
        if "Gold, gold, gold..." in player.quests:
            if poison in player.inventory:
                print("0. Leave bandit camp")
                print("1. Start a fight with the bunch of bandits.")
                print("2. Poison the cider.")

                choice = input("Choose: ")

                if choice == "0":
                    break

                elif choice == "1":
                    victory = battle(group_bandits, player)
                    if victory:
                        print("The bandits flee, but they leave a cart behind.")
                        player.quests_items.append("Cart")
                        pause()
                    else:
                        break

                elif choice == "2":
                    print("The bandits died.")
                    player.quests_items.append("Cart")
                    player.inventory.append(goods)
                    pause()
                else:
                    print("Invalid choice.")

            else:
                print("0. Leave bandit camp")
                print("1. Start a fight with the bunch of bandits.")
                choice = input("Choose: ")
                if choice == "0":
                    break
                elif choice == "1":
                    victory = battle(group_bandits, player)
                    if victory:
                        print("The bandits flee, but they leave a cart behind.")
                        player.quests_items.append("Cart")
                        pause()
                    else:
                        break

            if "Cart" in player.quests_items or "Goods" in player.inventory:
                print("0. Leave bandit camp")
                choice = input("Choose: ")
                if choice == "0":
                    break

        else:
            print("0. Leave bandit camp")
            print("1. Start a fight with the bandit.")
            choice = input("Choose: ")
            if choice == "0":
                break
            elif choice == "1":
                victory = battle(bandit, player)
                if victory:
                    pause()
                else:
                    break


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
