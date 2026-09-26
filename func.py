from random import randint
from units_lib import *


def battle(enemy: Enemy, player: Player):
    print("=" * 45)
    print(f"A BATTLE HAS STARTED: {enemy.name}")
    print("=" * 45)

    defending = False
    enemy_hp = enemy.health

    while enemy_hp > 0 and player.health > 0:
        print(f"{enemy.name} HP: {enemy_hp}/{enemy.health}")
        print(f"{player.name} HP: {player.health}/{player.max_health}")

        print("1. Attack")
        print("2. Defend")
        print("3. Heal")

        choice = input("Choose action: ")

        # Player attack
        if choice == "1":
            damage = randint(max(1, player.damage - 5), player.damage + 5)
            damage = max(1, damage - enemy.defense)
            enemy_hp -= damage
            print(f"You dealt {damage} damage!")
            defending = False

        # Player Defend
        elif choice == "2":
            print("You prepare to defend.")
            defending = True

        # Player Heal
        elif choice == "3":
            healing(player)
            continue

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")
            continue

        # Enemy attack
        if enemy_hp > 0:
            enemy_damage = randint(max(1, enemy.damage - 5), enemy.damage + 5)
            enemy_damage -= player.defense

            if defending:  # The protection parameter takes the value "True" when the player selects "2. Defend"
                enemy_damage //= 2
                print("\nYour defense reduced the damage!")

            enemy_damage = max(1, enemy_damage)
            player.health -= enemy_damage
            print(f"{enemy.name} dealt {enemy_damage} damage!")

    # Player dead
    if player.health <= 0:
        print("\nYou were defeated...")
        return False

    # Player victory
    print(f"You defeated {enemy.name}!")
    player.xp += enemy.xp
    player.gold += enemy.gold
    print(f"You received {enemy.gold} gold and {enemy.xp} XP.")
    check_level_up(player)
    return True


def healing(player: Player) -> bool:
    if player.health >= player.max_health:
        print(f"\nYour HP is already full ({player.health}/{player.max_health})!")
        pause()
        return False

    potions = [item for item in player.inventory if item.item_type == "potion"]

    if not potions:
        print("You have no potions in inventory!")
        pause()
        return False

    print("Your Potions:")
    print("0. Back (Cancel)")
    for idx, potion in enumerate(potions, start=1):
        print(f"{idx}. {potion.name} (+{potion.health_up} HP)")

    while True:
        try:
            potion_choice = int(input("Choose potion number: "))

            if potion_choice == 0:
                return False

            potion_idx = potion_choice - 1

            if 0 <= potion_idx < len(potions):
                selected_potion = potions[potion_idx]
                player.inventory.remove(selected_potion)
                player.health = min(
                    player.max_health,
                    player.health + selected_potion.health_up
                )
                print(
                    f"You used {selected_potion.name} and restored {selected_potion.health_up} HP!"
                )
                pause()
                return True
            else:
                print("Invalid potion number. Try again.")
        except ValueError:
            print("Please enter a number.")


def blacksmith(player: Player):
    while True:
        print("=" * 45)
        print("BLACKSMITH & EQUIPMENT")
        print(
            f"Your Gold: {player.gold} | Hero Level: {player.level} | Damage: {player.damage} | Defense: {player.defense}")

        print("-" * 45)
        gears = [item for item in player.inventory if item.item_type in ["weapon", "armor"]]
        if len(gears) > 0:
            gears = [item for item in player.inventory if item.item_type in ["weapon", "armor"]]
            if len(gears) > 0:
                print("Inventory:")
                for gear in gears:
                    if gear.item_type == "weapon":
                        print(
                            f"  • {gear.name} (Lvl {gear.level})|(+{gear.damage_bonus} Damage)|(Upgrade coef: {gear.coef_up})")
                    elif gear.item_type == "armor":
                        print(
                            f"  • {gear.name} (Lvl {gear.level})|(+{gear.defense_bonus} Defense)|(Upgrade coef: {gear.coef_up})")
            else:
                print("Inventory: Empty")
        if player.equipped_weapon:
            print(
                f"Weapon: {player.equipped_weapon.name} (Lvl {player.equipped_weapon.level}) "
                f"(+{player.equipped_weapon.damage_bonus} Damage)|(Upgrade coef:{player.equipped_weapon.coef_up})")
        else:
            print("Weapon: None")
        if player.equipped_armor:
            print(f"Armor: {player.equipped_armor.name} (Lvl {player.equipped_armor.level})|"
                  f"(+{player.equipped_armor.defense_bonus} Defense)|(Upgrade coef:{player.equipped_armor.coef_up})")
        else:
            print("Armor: None")
        print("=" * 45)

        print("0. Back")
        print("1. Equip item from Inventory")
        print("2. Unequip Weapon")
        print("3. Unequip Armor")
        print("4. Upgrade Equipped Weapon")
        print("5. Upgrade Equipped Armor")

        choice = input("Choose action: ")

        if choice == "0":
            break

        elif choice == "1":
            if not gears:
                print("No equipment in inventory!")
                pause()
                continue

            print("Select item to equip:")
            print("0. Back")
            for idx, gear in enumerate(gears, start=1):
                if gear.item_type == "weapon":
                    print(f"{idx}. {gear.name} (Lvl {gear.level})|"
                          f"(+{gear.damage_bonus} Damage)|(Upgrade coef:{gear.coef_up})")
                elif gear.item_type == "armor":
                    print(f"{idx}. {gear.name} (Lvl {gear.level})|"
                          f"(+{gear.defense_bonus} Defense)|(Upgrade coef:{gear.coef_up})")
            try:
                gear_choice = int(input("Choose item: "))
                if gear_choice == 0:
                    continue
                gear_idx = gear_choice - 1
                if 0 <= gear_idx < len(gears):
                    equip_item(player, gears[gear_idx])
                    pause()
                else:
                    print("Invalid choice.")
                    pause()
            except ValueError:
                print("Invalid input.")
                pause()

        elif choice == "2":
            unequip_weapon(player)
            pause()

        elif choice == "3":
            unequip_armor(player)
            pause()

        elif choice == "4":
            if player.equipped_weapon:
                print(
                    f"Upgrade this {player.equipped_weapon.name} (Lvl {player.equipped_weapon.level}) with {player.equipped_weapon.coef_up} coef for "
                    f"{player.equipped_weapon.upgrade_cost} gold? "
                    f"From {player.equipped_weapon.damage_bonus} damage -> to {round(player.equipped_weapon.damage_bonus * player.equipped_weapon.coef_up)} damage")
                choice2 = input("Upgrade? (yes/no): ")
                if choice2 == "yes":
                    upgrade_gear(player, player.equipped_weapon)
                elif choice2 == "no":
                    continue
            else:
                print("You don't have a weapon equipped!")
            pause()

        elif choice == "5":
            if player.equipped_armor:
                print(
                    f"Upgrade {player.equipped_armor.name} (Lvl {player.equipped_armor.level}) with {player.equipped_armor.coef_up} coef for "
                    f"{player.equipped_armor.upgrade_cost} gold? "
                    f"From {player.equipped_armor.defense_bonus} defense -> to {round(player.equipped_armor.defense_bonus * player.equipped_armor.coef_up)} damage")
                choice2 = input("Upgrade? (yes/no): ")
                if choice2 == "yes":
                    upgrade_gear(player, player.equipped_armor)
                elif choice2 == "no":
                    continue
                else:
                    print("Invalid choice.")
                    continue
            else:
                print("You don't have armor equipped!")
            pause()


def open_shop(player: Player):
    while True:
        print("\n" + "=" * 45)
        print("SHOP")
        print(f"Your Gold: {player.gold}")
        print("=" * 45)
        print("0. Leave shop")
        print("1. Buy items")
        print("2. Sell items")
        action = input("\nChoose action: ")

        if action == "0":
            print("\nThanks for visiting!")
            pause()
            break

        elif action == "1":
            while True:
                print("\n" + "-" * 45)
                print("BUY ITEMS")
                print(f"Your Gold: {player.gold}")
                print("-" * 45)
                print("0. Back to main shop menu")

                for idx, item in enumerate(shop_inventory, start=1):
                    in_inv = any(
                        inv_item.name == item.name for inv_item in player.inventory
                    )
                    in_wpn = (
                            player.equipped_weapon
                            and player.equipped_weapon.name == item.name
                    )
                    in_arm = (
                            player.equipped_armor and player.equipped_armor.name == item.name
                    )

                    has_item = in_inv or in_wpn or in_arm
                    status = "[OWNED]" if has_item else f"{item.cost} Gold"

                    if item.item_type == "weapon":
                        print(
                            f"{idx}. {item.name} (Lvl {item.level}) | (+{item.damage_bonus}"
                            f" Damage) | Coef: {item.coef_up} — {status}"
                        )
                    elif item.item_type == "armor":
                        print(
                            f"{idx}. {item.name} (Lvl {item.level}) | (+{item.defense_bonus}"
                            f" Defense) | Coef: {item.coef_up} — {status}"
                        )
                    elif item.item_type == "potion":
                        print(f"{idx}. {item.name} (+{item.health_up} HP) — {status}")
                    else:
                        print(f"{idx}. {item.name} — {status}")

                choice = input("\nChoose an item to buy: ")

                if choice == "0":
                    break
                try:
                    item_idx = int(choice) - 1
                    if 0 <= item_idx < len(shop_inventory):
                        selected_item = shop_inventory[item_idx]
                        in_inv = any(
                            inv_item.name == selected_item.name
                            for inv_item in player.inventory
                        )
                        in_wpn = (
                                player.equipped_weapon
                                and player.equipped_weapon.name == selected_item.name
                        )
                        in_arm = (
                                player.equipped_armor
                                and player.equipped_armor.name == selected_item.name
                        )

                        already_has = in_inv or in_wpn or in_arm

                        if already_has:
                            print(
                                f"\nYou already have {selected_item.name}! You can only hold"
                                " one of each."
                            )
                        elif player.gold < selected_item.cost:
                            print("\nYou don't have enough gold!")
                        else:
                            player.gold -= selected_item.cost
                            player.inventory.append(selected_item)
                            print(
                                f"\nYou bought {selected_item.name} for {selected_item.cost}"
                                " gold!"
                            )
                    else:
                        print("\nInvalid choice.")
                except ValueError:
                    print("\nPlease enter a number.")

        elif action == "2":
            while True:
                print("\n" + "-" * 45)
                print("SELL ITEMS")
                print(f"Your Gold: {player.gold}")
                print("-" * 45)
                print("0. Back to main shop menu")

                if not player.inventory:
                    print("\nYour inventory is empty!")
                    break

                for idx, item in enumerate(player.inventory, start=1):
                    if item.item_type == "weapon" or item.item_type == "armor":
                        sell_price = item.cost + ((item.level - 1) * item.upgrade_cost)
                        print(f"{idx}. {item.name} (Lvl {item.level}) — Sell for {sell_price} Gold")
                    elif item.item_type == "potion":
                        sell_price = item.cost
                        print(f"{idx}. {item.name} (+{item.health_up} HP) — Sell for {sell_price} Gold")
                    else:
                        sell_price = item.cost
                        print(f"{idx}. {item.name} — Sell for {sell_price} Gold")

                choice = input("\nChoose an item to sell: ")

                if choice == "0":
                    break

                try:
                    item_idx = int(choice) - 1

                    if 0 <= item_idx < len(player.inventory):
                        sold_item = player.inventory.pop(item_idx)
                        if sold_item.item_type == "weapon" or sold_item.item_type == "armor":
                            sell_price = sold_item.cost + ((sold_item.level - 1) * sold_item.upgrade_cost)
                            player.gold += sell_price
                            print(
                                f"\nYou sold {sold_item.name} (Lvl {sold_item.level}) for {sell_price} gold!"
                            )
                        else:
                            sell_price = sold_item.cost
                            player.gold += sell_price
                            print(
                                f"\nYou sold {sold_item.name} for {sell_price} gold!"
                            )
                    else:
                        print("\nInvalid choice.")
                except ValueError:
                    print("\nPlease enter a number.")

        else:
            print("\nInvalid choice.")


def check_level_up(player: Player):
    xp_needed = player.level * 50

    if player.xp >= xp_needed:
        player.level += 1
        player.xp -= xp_needed

        player.max_health += 10
        player.health = player.max_health
        player.damage += 2
        player.defense += 1

        print("*" * 45)
        print(f"LEVEL UP! You reached Level {player.level}!")
        print(f"Max HP increased to {player.max_health} (Fully Restored!)")
        print(f"Damage increased to {player.damage}")
        print(f"Defense increased to {player.defense}")
        print("*" * 45)


def chek_param(player: Player):
    print("=" * 45)
    print(f"Name: {player.name}")
    print(f"HP: {player.health}/{player.max_health}")
    print(f"XP: {player.xp}")
    print(f"Level: {player.level}")
    print(f"Reputation: {player.reputation}")
    print(f"Damage: {player.damage}")
    print(f"Defense: {player.defense}")
    print("=" * 45)
    pause()


def chek_inventory(player: Player):
    print("=" * 45)
    print(f"Name: {player.name}")
    print(f"Gold: {player.gold}")

    if player.equipped_weapon:
        print(
            f"Weapon: {player.equipped_weapon.name} (LVL {player.equipped_weapon.level}) "
            f"(+{player.equipped_weapon.damage_bonus} Damage)|(Damage coef:{player.equipped_weapon.coef_up})")
    else:
        print("Weapon: None")

    if player.equipped_armor:
        print(
            f"Armor: {player.equipped_armor.name} (LVL {player.equipped_armor.level}) "
            f"(+{player.equipped_armor.defense_bonus} Defense)|(Defense coef:{player.equipped_armor.coef_up})")
    else:
        print("Armor: None")

    if len(player.artifacts) > 0:
        print(f"Artifacts: {', '.join(player.artifacts)}")
    else:
        print("Artifacts: Empty")

    if len(player.inventory) > 0:
        print(f"Inventory:")
        print("-" * 45)
        for idx, item in enumerate(player.inventory, start=1):
            if item.item_type == "weapon":
                print( f"{idx}. Weapon: {item.name} (LVL {item.level}) "
                f"(+{item.damage_bonus} Damage)|(Damage coef:{item.coef_up})")
            elif item.item_type == "armor":
                print(
                    f"{idx}. Armor: {item.name} (LVL {item.level}) "
                    f"(+{item.defense_bonus} Defense)|(Defense coef:{item.coef_up})")
            elif item.item_type == "potion":
                print(f"{idx}. {item.name} (+{item.health_up} HP)")
            else:

                print(f"{idx}. {item.name}")
        print("-" * 45)
    else:
        print("Inventory: Empty")

    if len(player.quests_items) > 0:
        print(f"Quests items: {', '.join(player.quests_items)}")
    else:
        print("Quests items: Empty")


    has_potions = any(item.item_type == "potion" for item in player.inventory)
    if has_potions:
        print("-" * 45)
        while True:
            choice = input("Do you want to heal? (yes/no): ").lower()
            if choice == "yes":
                healing(player)
                break
            elif choice == "no":
                break
            else:
                print("Invalid choice.")

    print("=" * 45)
    pause()


def chek_quests(player: Player):
    print("=" * 45)

    print("Active quests:")
    if player.quests:
        for quest in player.quests:
            print(f" - {quest}")
    else:
        print(" - No active quests")

    print("-" * 45)

    print("Completed quests:")
    if player.completed_quests:
        for quest in player.completed_quests:
            print(f" - {quest}")
    else:
        print(" - No completed quests")



    print("=" * 45)
    pause()


def unequip_weapon(player: Player):
    if player.equipped_weapon:
        item = player.equipped_weapon
        player.damage -= item.damage_bonus
        player.inventory.append(item)
        player.equipped_weapon = None
        print(f"Unequipped {item.name}. (-{item.damage_bonus} Damage)")
    else:
        print("No weapon equipped!")


def unequip_armor(player: Player):
    if player.equipped_armor:
        item = player.equipped_armor
        player.defense -= item.defense_bonus
        player.inventory.append(item)
        player.equipped_armor = None
        print(f"Unequipped {item.name}. (-{item.defense_bonus} Defense)")
    else:
        print("No armor equipped!")


def equip_item(player: Player, item):
    if item.item_type == "weapon":

        if player.equipped_weapon:
            player.damage -= player.equipped_weapon.damage_bonus
            player.inventory.append(player.equipped_weapon)

        # Вдягаємо нову зброю та додаємо її бонус
        player.equipped_weapon = item
        player.damage += item.damage_bonus
        player.inventory.remove(item)
        print(f"You equipped {item.name}! (+{item.damage_bonus} Damage)")

    elif item.item_type == "armor":

        if player.equipped_armor:
            player.defense -= player.equipped_armor.defense_bonus
            player.inventory.append(player.equipped_armor)

        player.equipped_armor = item
        player.defense += item.defense_bonus
        player.inventory.remove(item)
        print(f"You equipped {item.name}! (+{item.defense_bonus} Defense)")


def upgrade_gear(player: Player, gear):
    if gear.level >= player.level:
        print(f"You cannot upgrade {gear.name} higher than your Hero Level ({player.level})!")
        return

    if player.gold < gear.upgrade_cost:
        print(f"Not enough gold! Cost: {gear.upgrade_cost} Gold.")
        return

    player.gold -= gear.upgrade_cost
    gear.level += 1

    if gear.item_type == "weapon":
        gear.damage_bonus = round(gear.damage_bonus * gear.coef_up)

        if player.equipped_weapon == gear:
            player.damage += gear.damage_bonus

        print(f"{gear.name} upgraded to Level {gear.level}! Damage bonus: +{gear.damage_bonus}")

    elif gear.item_type == "armor":
        gear.defense_bonus = round(gear.defense_bonus * gear.coef_up)

        if player.equipped_armor == gear:
            player.defense += gear.defense_bonus

        print(f"{gear.name} upgraded to Level {gear.level}! Defense bonus: +{gear.defense_bonus}")

    gear.upgrade_cost = int(gear.upgrade_cost * 1.5)


def pause():
    input("Press ENTER to continue...")
