# menu.py
'''
Module for the game Title Screen
'''
from settings import Settings

def display_main_menu():
    print("Welcome to Connect 4!")
    print("1. Start New Game")
    print("2. Load Saved Game")
    print("3. Customize Settings")
    print("4. Create New Account")
    print("5. Quit")

def customize_settings():
    settings = Settings()
    settings.load_settings()
    
    print("Customizing settings...")
    
    # Get player customization inputs
    player1_name = input("Enter Player 1's username: ")
    player2_name = input("Enter Player 2's username: ")
    player1_piece = input(f"Enter {player1_name}'s piece type (e.g., 'X'): ")
    player2_piece = input(f"Enter {player2_name}'s piece type (e.g., 'O'): ")
    player1_color = input(f"Enter {player1_name}'s color (e.g., 'red'): ")
    player2_color = input(f"Enter {player2_name}'s color (e.g., 'blue'): ")
    
    # Update player settings directly in the Settings object
    settings.users[player1_name]['piece'] = player1_piece
    settings.users[player1_name]['color'] = player1_color
    settings.users[player2_name]['piece'] = player2_piece
    settings.users[player2_name]['color'] = player2_color
    
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
    new_color = input("Enter your desired color (e.g., 'red'): ")
    
    # Check if the username already exists
    if new_username in settings.users:
        print("Username already exists. Please choose another one.")
        return
    
    # Add the new account to settings
    settings.users[new_username] = {'piece': new_piece, 'color': new_color}
    
    # Save settings to file
    settings.save_settings()
    
    print("Account created successfully.")

def main_menu():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("Starting a new game...")
            # Call a function to start a new game
        elif choice == "2":
            print("Loading a saved game...")
            # Call a function to load a saved game
        elif choice == "3":
            customize_settings()
        elif choice == "4":
            create_new_account()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()