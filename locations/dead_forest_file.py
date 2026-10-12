import time
from units_lib import Player, Enemy
from framefunc import pause, mission_append, mission_complete
from func import battle


def dead_forest(player: Player):
    while True:
        if "Past glory" in player.completed_quests:
            print("=" * 45)
            print("DEAD FOREST")
            print("=" * 45)
            print("***A thick, ghostly fog blankets the dead forest.***")
            time.sleep(2.5)
            if "Ash Blessing" in player.quests_items:
                print("***The fog parts before you, recognizing the carrier of the Ash Blessing***")
                print("0. Leave the Dead Forest")
                choice = input("Choose: ")
                if choice == "0":
                    return
            else:
                mission_append(player, "Whispers of the Dead")
                time.sleep(2)
                print("0. Leave the Dead Forest")
                print("1. Approach the Altar of Reflection")
                choice = input("Choose: ")
                if choice == "0":
                    return
                elif choice == "1":
                    print(
                        "\n*** As you step near the altar, the black fog gathers into a figure matching your shape. ***")
                    time.sleep(3)
                    print("Ancient Spirits: 'To earn our blessing, you must defeat your reflection in combat.'")
                    time.sleep(3)
                    shadow = Enemy(
                        name="Shadow Self",
                        health=player.health,
                        damage=player.damage,
                        defense=player.defense,
                        xp=50,
                        gold=0
                    )
                    victory = battle(shadow, player)
                    if victory:
                        print("\n*** The spirits bow before your strength and mastery. ***")
                        time.sleep(3)
                        print("You received the Ash Blessing!")

                        player.quests_items.append("Ash Blessing")
                        mission_complete(player, "Whispers of the Dead")
                        pause()
                        return
                    else:
                        pause()
                        return
                else:
                    print("Invalid choice.")
        else:
            print(
                "***This is still too far away for you***")
            pause()
            return
