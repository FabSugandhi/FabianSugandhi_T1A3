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
        settings["piece"] = piece
        settings["color"] = color
        self.users[username] = settings

    # Other methods for accessing and modifying settings...

# Example usage:
if __name__ == "__main__":
    settings = Settings()
    settings.load_settings()
    settings.add_user("New User", "X", "red")  # Add a new user with default settings
    settings.save_settings()