import pickle
import os
from units_lib import Player


def save_game(player: Player):
    filename = f"save_{player.name}.pkl"
    try:
        with open(filename, "wb") as file:
            pickle.dump(player, file)
        print(f"Game for {player.name} is successfully  saved in {filename}!")
    except Exception as e:
        print(f"Error: {e}")
    pause()


def load_game_by_name() -> Player:
    saves = [file for file in os.listdir() if file.startswith("save_") and file.endswith(".pkl")]

    if not saves:
        print("There are no saved games.")
        pause()
        return None

    print("=" * 45)
    print("SAVES: ")
    print("=" * 45)
    print("0. Quit")

    for idx, save_file in enumerate(saves, start=1):
        player_name = save_file.replace("save_", "").replace(".pkl", "")
        print(f"{idx}. {player_name}")

    try:
        choice = int(input("Choose number of saving: "))
        if choice == 0:
            return None

        if 1 <= choice <= len(saves):
            selected_file = saves[choice - 1]
            with open(selected_file, "rb") as f:
                player = pickle.load(f)
            print(f"Player is loaded: {player.name}!")
            pause()
            return player
        else:
            print("Invalid choice.")
            pause()
            return None
    except ValueError:
        print("Please choose a number.")
        pause()
        return None


def mission_complete(player: Player, mission_name: str):
    if mission_name in player.quests:
        player.quests.remove(mission_name)

    if mission_name not in player.completed_quests:
        player.completed_quests.append(mission_name)

    print(f"Quest === {mission_name} === completed")


def pause():
    input("Press ENTER to continue...")
