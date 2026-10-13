import time

from framefunc import load_game_by_name, save_game
from func import *

from units_lib import Player

from locations import village, bandit_camp, forest, lake, old_ruins, bridge, dragon_slayers_guild, temple_of_fire, \
    dead_forest, bear_cave, northern_pass, dragon_lair, sorcerer_tower


# Stable internal keys are saved on the Player object; display labels can change safely.
LOCATION_OPTIONS = [
    ("Village", "Eldoria Village", village),
    ("Bandit Camp", "Bandit Camp", bandit_camp),
    ("Forest", "Forest", forest),
    ("Lake", "Lake", lake),
    ("Bridge", "Bridge", bridge),
    ("Dragon Slayers' Guild", "Dragon Slayers' Guild", dragon_slayers_guild),
    ("Old Ruins", "Old Ruins", old_ruins),
    ("Dead Forest", "Dead Forest", dead_forest),
    ("Temple of Fire", "Temple of Fire", temple_of_fire),
    ("Bear Cave", "Bear Cave", bear_cave),
    ("Northern Mountain Pass", "Northern Mountain Pass", northern_pass),
    ("Dragon's Lair", "Dragon's Lair", dragon_lair),
    ("Sorcerer's Tower", "Sorcerer's Tower", sorcerer_tower),
]


def update_unlocked_locations(player: Player):
    """Unlock locations based on story progress, without ever locking them again.

    Also upgrades older save files that were created before unlocked_locations existed.
    """
    if not isinstance(getattr(player, "unlocked_locations", None), list):
        player.unlocked_locations = ["Village"]

    if "Village" not in player.unlocked_locations:
        player.unlocked_locations.insert(0, "Village")

    active_quests = set(getattr(player, "quests", []))
    completed_quests = set(getattr(player, "completed_quests", []))
    artifacts = set(getattr(player, "artifacts", []))
    quest_items = set(getattr(player, "quests_items", []))

    story_rules = {
        "Forest": (
            "Old Stories" in active_quests
            or "Old Stories" in completed_quests
        ),
        "Bandit Camp": (
            "Gold, gold, gold..." in active_quests
            or "Gold, gold, gold..." in completed_quests
            or "Cart" in quest_items
        ),
        "Lake": (
            "One Wish" in active_quests
            or "One Wish" in completed_quests
        ),
        "Bridge": (
            "One Wish" in completed_quests
            or "Charity" in active_quests
            or "Charity" in completed_quests
        ),
        "Dragon Slayers' Guild": (
            "Charity" in active_quests
            or "Charity" in completed_quests
        ),
        "Old Ruins": "Eye of Truth" in artifacts,
        "Dead Forest": "Past glory" in completed_quests,
        "Temple of Fire": (
            "Heroes of the Past" in completed_quests
            and "Past glory" in completed_quests
        ),
        "Bear Cave": "Flame Trial" in completed_quests,
        "Northern Mountain Pass": "Flame Trial" in completed_quests,
        "Dragon's Lair": "Frozen Secrets" in completed_quests,
        "Sorcerer's Tower": "Dragon's Blessing" in quest_items,
    }

    for location_key, is_unlocked in story_rules.items():
        if is_unlocked and location_key not in player.unlocked_locations:
            player.unlocked_locations.append(location_key)


def main():
    print("=" * 55)
    print(" THE LAST FLAME")
    print("=" * 55)

    player = None

    print("1. New game")
    print("2. Load saved game")
    start_choice = input("Choose option: ").strip()

    if start_choice == "1":
        print("Now the dragon is awakening.")
        print("Five ancient artifacts are the only things that can stop what is coming.")

        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        player = Player(name)
        print(f"Welcome, {player.name}!")
        time.sleep(2)

    elif start_choice == "2":
        player = load_game_by_name()

        if player is None:
            print("Loading cancelled. Exiting game.")
            return

    else:
        print("Invalid choice. Exiting game.")
        return

    # This also restores story-unlocked locations for saves made by older versions.
    update_unlocked_locations(player)

    while player.health > 0:
        # Re-check after returning from a location, because its quests may have changed.
        update_unlocked_locations(player)

        print("=" * 45)
        print("MAIN MENU")
        print("=" * 45)

        available_locations = [
            (key, label, function)
            for key, label, function in LOCATION_OPTIONS
            if key in player.unlocked_locations
        ]

        menu_actions = {}
        for index, (key, label, function) in enumerate(available_locations, start=1):
            print(f"{index}. {label}")
            menu_actions[str(index)] = function

        stats_choice = len(available_locations) + 1
        inventory_choice = stats_choice + 1
        quests_choice = stats_choice + 2
        quit_choice = stats_choice + 3

        print(f"{stats_choice}. Check your parameters and stats")
        print(f"{inventory_choice}. Check your inventory")
        print(f"{quests_choice}. Check quests")
        print(f"{quit_choice}. Quit game")
        print("+. Save game")

        choice = input("Choose destination: ").strip()

        if choice in menu_actions:
            menu_actions[choice](player)

        elif choice == str(stats_choice):
            chek_param(player)

        elif choice == str(inventory_choice):
            chek_inventory(player)

        elif choice == str(quests_choice):
            chek_quests(player)

        elif choice == str(quit_choice):
            print("Thank you for playing The Last Flame!")
            break

        elif choice == "+":
            save_game(player)

        else:
            print("Invalid choice.")
            pause()

    if player.health <= 0:
        print("=" * 45)
        print("GAME OVER")
        print("=" * 45)
        print("Your journey has come to an end.")


if __name__ == "__main__":
    main()
