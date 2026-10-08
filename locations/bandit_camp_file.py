from units_lib import Player, poison, goods, group_bandits, bandit
from framefunc import pause
from func import battle

import time


def bandit_camp(player: Player):
    while True:
        print("=" * 45)
        print("BANDIT CAMP")
        print("=" * 45)

        has_poison = any(item.name == "Poison" for item in player.inventory)
        has_cart = "Cart" in player.quests_items
        has_goods = any(item.name == "Goods" for item in player.inventory)

        if "Gold, gold, gold..." in player.quests:
            if has_cart or has_goods:
                print("The bandit camp is quiet now.")
                print("0. Leave bandit camp")
                choice = input("Choose: ")
                if choice == "0":
                    break
                continue

            print("0. Leave bandit camp")
            print("1. Start a fight with the bunch of bandits.")
            if has_poison:
                print("2. Poison the cider.")

            choice = input("Choose: ")

            if choice == "0":
                break

            elif choice == "1":
                victory = battle(group_bandits, player)
                if victory:
                    print("***The bandits flee, but they leave a cart behind.***")
                    player.quests_items.append("Cart")
                    print("+ Cart")
                    pause()
                else:
                    break

            elif choice == "2" and has_poison:
                player.inventory.remove(poison)
                print("***You secretly poison the cider. The bandits drink it and fall unconscious!***")
                time.sleep(2)
                player.quests_items.append("Cart")
                player.inventory.append(goods)
                print("+ Cart")
                print("+ Goods")
                pause()

            else:
                print("Invalid choice.")

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
