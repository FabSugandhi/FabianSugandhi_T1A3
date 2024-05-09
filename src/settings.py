# settings.py
'''
Module for the player settings
'''

import json

class Settings:
    def __init__(self):
        self.users = {}

    def load_settings(self, filename="settings.json"):
        try:
            with open(filename, "r") as json_file:
                self.users = json.load(json_file)
                # Ensure that matches_won and matches_lost fields are present for each user
                for user_settings in self.users.values():
                    user_settings.setdefault("matches_won", 0)
                    user_settings.setdefault("matches_lost", 0)
        except FileNotFoundError:
            print(f"Settings file '{filename}' not found. Using default settings.")

    def save_settings(self, filename="settings.json"):
        with open(filename, "w") as json_file:
            json.dump(self.users, json_file, indent=4)

    def add_user(self, username, piece, color, settings=None):
        if settings is None:
            # Use default settings if none provided
            default_settings = self.users.get("Default", {})
            settings = default_settings.copy()
            settings["player_name"] = username
            settings["matches_won"] = 0  # Initialize matches won to 0
            settings["matches_lost"] = 0  # Initialize matches lost to 0
        settings["piece"] = piece
        settings["color"] = color
        self.users[username] = settings

    def update_match_history(self, winner, loser):
        if winner in self.users:
            self.users[winner]['matches_won'] += 1
        else:
            print(f"User '{winner}' not found.")

        if loser in self.users:
            self.users[loser]['matches_lost'] += 1
        else:
            print(f"User '{loser}' not found.")

        self.save_settings()

    def get_match_history(self, username):
        if username in self.users:
            return {
                "matches_won": self.users[username]["matches_won"],
                "matches_lost": self.users[username]["matches_lost"]
            }
        else:
            print(f"User '{username}' not found.")
            return None
    # Other methods for accessing and modifying settings...

# Example usage:
if __name__ == "__main__":
    settings = Settings()
    settings.load_settings()
    settings.add_user("New User", "X", "red")  # Add a new user with default settings
    settings.save_settings()