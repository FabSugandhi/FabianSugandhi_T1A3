# game.py
'''
Module for the game logic
'''
from settings import Settings

class Connect4Game:
    def __init__(self, player1, player2):
        # Initialize game state
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.settings = Settings()
        self.settings.load_settings()

    def display_board(self):
        # Display the game board
        print("+---+---+---+---+---+---+---+")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("+---+---+---+---+---+---+---+")
        print("  1   2   3   4   5   6   7")
 
    def drop_piece(self, column):
        if not 1 <= column <= 7:
            print("Invalid column number. Please choose a column between 1 and 7.")
            return False

        column -= 1  # Adjust for zero-based indexing
        for i in range(5, -1, -1):
            if self.board[i][column] == ' ':
                current_piece = self.settings.users[self.current_player]['piece']
                self.board[i][column] = current_piece
                # Check for a winner
                if self.check_winner(current_piece, i, column):  
                    print(f"Player {self.current_player} wins!")
                    return True
                # Check for a draw
                if self.check_draw():  
                    print("The game is a draw!")
                    return True
                # Switch to the next player's turn
                self.switch_player()  
                return True
        print("Column is full. Please choose another column.")
        return False
    
    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def check_winner(self, piece, row, col):
        # Check for four pieces in a row
        for c in range(4):
            if col + c < 4 and all(self.board[row][col+c+i] == piece for i in range(4)):
                return True
        # Check for four pieces in a column
        for r in range(3):
            if row + r < 3 and all(self.board[row+r+i][col] == piece for i in range(4)):
                return True
        # Check for four pieces in a diagonal (top-left to bottom-right)
        for d in range(4):
            if row - d >= 0 and col - d >= 0 and row + 3 - d < 6 and col + 3 - d < 7 and \
                all(self.board[row+i-d][col+i-d] == piece for i in range(4)):
                return True
        # Check for four pieces in a diagonal (bottom-left to top-right)
        for d in range(4):
            if row + d < 6 and col - d >= 0 and row - 3 + d >= 0 and col + 3 - d < 7 and \
                all(self.board[row-i+d][col+i-d] == piece for i in range(4)):
                return True
        return False
    
    def check_draw(self):
        # Check if the board is full (no empty spaces)
        return all(cell != ' ' for row in self.board for cell in row)

if __name__ == "__main__":
    # Test code
    game = Connect4Game("Player 1", "Player 2")
    game.display_board()
    for column in range (1,8):
        for _ in range(6):
            game.drop_piece(column)
    # This move should result in a draw