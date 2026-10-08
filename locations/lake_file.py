from units_lib import Player, rod, fish
from framefunc import pause
from func import fishing


def lake(player: Player):
    while True:
        print("=" * 45)
        print("LAKE")
        print("=" * 45)
        print("0. Leave Lake")
        print("1. To fish")

        choice = input("Choose: ")
        if choice == "0":
            break
        elif choice == "1":
            if rod not in player.inventory:
                print("You don't have a rod")
                pause()
            else:
                if "One Wish" in player.quests:
                    if "Orb of Wishes" in player.quests_items:
                        print("You’ve already caught the magic fish")
                        pause()
                    else:
                        fishing(player, quest_param=True)
                        pause()
                else:
                    if fish in player.inventory:
                        print("You cannot catch more fish.")
                        pause()
                    else:
                        fishing(player, quest_param=False)
                        pause()