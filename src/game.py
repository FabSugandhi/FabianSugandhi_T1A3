# game.py
'''
Module for the game logic
'''

class Connect4Game:
    def __init__(self, player1, player2):
        # Initialize game state
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = [[' ' for _ in range(7)] for _ in range(6)]

    def display_board(self):
        # Display the game board
        print("+---+---+---+---+---+---+---+")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("+---+---+---+---+---+---+---+")
        print("  1   2   3   4   5   6   7")

if __name__ == "__main__":
    # Test code
    game = Connect4Game("Player 1", "Player 2")
    game.display_board()