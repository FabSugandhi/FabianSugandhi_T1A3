# settings.py
'''
Module for the player settings
'''

import json

class Settings:
    def __init__(self):
        self.users = {}  # Dictionary to store user accounts

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = {
                'player1_name': "Player 1",
                'player2_name': "Player 2",
                'player1_piece': "X",
                'player2_piece': "O",
                'player1_color': "Red",
                'player2_color': "Yellow",
                'match_history': []
            }
            return True
        else:
            print("Username already exists. Please choose a different username.")
            return False

    def save_settings(self, filename='settings.json'):
        with open(filename, 'w') as f:
            json.dump(self.users, f)

    def load_settings(self, filename='settings.json'):
        try:
            with open(filename, 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            print("Settings file not found. Creating a new one.")

if __name__ == "__main__":
    settings = Settings()
    settings.load_settings()
    settings.create_user("user1")
    settings.save_settings()