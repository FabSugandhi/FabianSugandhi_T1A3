# menu.py
'''
Module for the game Title Screen
'''
def display_title_screen():
    print("Welcome to Connect 4!")
    print("1. Start New Game")
    print("2. Load Saved Game") #Need to implement
    print("3. Customize Settings") #Need to implement
    print("4. Quit")

def main_menu():
    while True:
        display_title_screen()
        choice = input("Enter your choice: ")

        if choice == "1":
            start_new_game()
        elif choice == "2":
            load_saved_game() #Need to implement
        elif choice == "3":
            customize_settings() #Need to implement
        elif choice == "4":
            print ("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number from 1 to 4")

def start_new_game():
    print("Starting new game...")
    # Implement game initialization logic here

def load_saved_game():
    print("Loading saved game...")
    #Implement game loading logic here

def customize_settings():
    print("Customizing settings...")
    #Implement settings customization logic here

if __name__ == "__main__":
    main_menu()