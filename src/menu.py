# menu.py
'''
Module for the game Title Screen
'''
from colorama import init, Style
init() 
from game import Connect4Game
# Import the Connect4Game class from game.py
from settings import Settings
import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    print("Welcome to Connect 4!")
    print("1. Start New Game")
    print("2. Customize Settings")
    print("3. Create New Account")
    print("4. Quit")

def customize_settings():
    settings = Settings()
    settings.load_settings()
    
    print("Customizing settings...")
    
    # Initialize variables
    player1_name = input("Enter Player 1's username: ")
    player1_piece = None
    player1_color = None
    
    # Check if the player is not found in the settings
    if player1_name not in settings.users:
        print(f"{player1_name} is not registered, please create a new account.")
        create_new_account()
    else:
        # Player found, proceed with customization
        player1_piece = input(f"Enter {player1_name}'s piece type (e.g., 'X'): ")
        player1_color = input(f"Enter {player1_name}'s color (e.g., 'red'): ")
    
    # Update player settings directly in the Settings object if player is found
    if player1_piece is not None and player1_color is not None:
        settings.users[player1_name]['piece'] = player1_piece
        settings.users[player1_name]['color'] = player1_color
        
        # Save settings to file
        settings.save_settings()
        print("Settings saved.")

def create_new_account():
    settings = Settings()
    settings.load_settings()
    
    print("Creating a new account...")
    
    # Get account information
    new_username = input("Enter your desired username: ")
    new_piece = input("Enter your desired piece type (e.g., 'X'): ")
    
     # Keep prompting until a valid color is entered
    while True:
        new_color = input("Enter your desired color (valid colors are: red, green, yellow, blue, magenta, cyan, white.): ").lower()  # Convert to lowercase for consistency
        
        # Check if the entered color is valid
        if new_color in ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
            break  # Exit the loop if a valid color is entered
        else:
            print("Invalid color. Please choose from: red, green, yellow, blue, magenta, cyan, white.")
    
    # Check if the username already exists
    if new_username in settings.users:
        print("Username already exists. Please choose another one.")
        return
    
    # Add the new account to settings
    settings.users[new_username] = {'piece': new_piece, 'color': new_color}
    
    # Save settings to file
    settings.save_settings()
    
    print("Account created successfully.")

def start_new_game():
    # Load settings from the JSON file
    settings = Settings()
    settings.load_settings()
  
   # Get player names from user input
    player1_name = input("Enter Player 1's username: ")
    player2_name = input("Enter Player 2's username: ")
    
    # Check if any of the players are not in the settings
    if player1_name not in settings.users or player2_name not in settings.users:
        print("One or both players are not found")
        if player1_name not in settings.users:
            print(f"{player1_name} is not registered, please create new account.")
            create_new_account()
        if player2_name not in settings.users:
            print(f"{player2_name} is not registered, please create new account.")
            create_new_account()
        
        # Reload settings after creating new accounts
        settings.load_settings()
    
    # Get pieces and colors from settings
    player1_piece = settings.users[player1_name]['piece']
    player2_piece = settings.users[player2_name]['piece']
    player1_color = settings.users[player1_name]['color']
    player2_color = settings.users[player2_name]['color']

    # Create an instance of the Connect4Game class with player names, pieces, and colors
    game = Connect4Game(player1_name, player2_name)
    game.settings = settings  # Pass the settings object to the game instance
    game.settings.users[player1_name]['piece'] = player1_piece
    game.settings.users[player1_name]['color'] = player1_color
    game.settings.users[player2_name]['piece'] = player2_piece
    game.settings.users[player2_name]['color'] = player2_color
    
    # Call the play method to start the game
    game.play()

def main_menu():
    while True:
        clear_screen()  # Clear the screen before displaying the main menu
        display_main_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("Starting a new game...")
            # Call a function to start a new game
            start_new_game()
        elif choice == "2":
            customize_settings()
        elif choice == "3":
            create_new_account()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()