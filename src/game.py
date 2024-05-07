# game.py
'''
Module for the game logic
'''

class Connect4Game:
    def __init__(self, username):
        self.username = username
        # Initialize game state
        pass

    def display_board(self):
        # Display the game board
        pass

    def make_move(self, column):
        # Make a move
        pass

    def check_winner(self):
        # Check for a winner
        pass

    def switch_player(self):
        # Switch player
        pass

    def play(self):
        # Main game loop
        while True:
            self.display_board()
            column = self.get_player_move()
            if self.make_move(column):
                if self.check_winner():
                    self.display_board()
                    print(f"Congratulations {self.current_player.name}! You win!")
                    break
                if self.board_full():
                    self.display_board()
                    print("It's a tie!")
                    break
                self.switch_player()

    def get_player_move(self):
        # Get player move input
        pass

    def board_full(self):
        # Check if the board is full
        pass

if __name__ == "__main__":
    # Test code
    pass