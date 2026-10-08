from units_lib import Player, goods
import time
from func import open_shop, blacksmith
from framefunc import pause, mission_complete


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

            if "Old Stories" not in player.quests and "Old Stories" not in player.completed_quests:
                print("ELDER:")
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
                time.sleep(3)

                player.quests.append("Old Stories")
                print("\nYou got a new quest!")
                print("=== Old Stories ===")
                time.sleep(1.5)
                pause()

            elif "Old Stories" in player.quests:
                print("Elder: Time flies....")
                time.sleep(1.5)
                pause()

            elif "Old Stories" in player.completed_quests:
                print(
                    "Elder: You survived, and that's good."
                )
                time.sleep(1.5)
                pause()


        elif choice == "2":
            # 1. Quest already completed
            if "Gold, gold, gold..." in player.completed_quests:
                print("Merchant: Thank you for your help!")
                pause()
            # 2. Quest active in player's quest log
            elif "Gold, gold, gold..." in player.quests:
                has_goods = goods in player.inventory  # Replace "Goods" with your variable if applicable
                has_cart = "Cart" in player.quests_items
                # Full success: Returned both Cart and Goods
                if has_cart and has_goods:
                    print("Merchant: Thank you for your help!")
                    time.sleep(3)
                    player.inventory.remove(goods)
                    print("-Goods")
                    player.quests_items.remove("Cart")
                    print("-Cart")
                    time.sleep(3)
                    player.gold += 15
                    player.xp += 20
                    player.reputation += 15
                    print(f"You got 15 gold and 20 XP! Your gold is {player.gold} and XP is {player.xp}")
                    print(f"Your reputation is {player.reputation}")
                    time.sleep(3)
                    mission_complete(player, "Gold, gold, gold...")
                    time.sleep(3)
                    pause()
                # Partial success: Returned Cart only
                elif has_cart and not has_goods:
                    print("Merchant: Thank you for your help!")
                    player.quests_items.remove("Cart")
                    print("-Cart")
                    player.gold += 5
                    player.xp += 10
                    print(f"You got 5 gold and 10 XP! Your gold is {player.gold} and XP is {player.xp}")
                    time.sleep(3)
                    mission_complete(player, "Gold, gold, gold...")
                    time.sleep(3)
                    pause()
                # Still in progress (has neither or hasn't retrieved the cart yet)
                else:
                    print("Merchant: Sorry I am busy...")
                    time.sleep(1.5)
                    pause()
            # 3. Quest not started yet
            else:
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