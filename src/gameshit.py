from settings import Settings
import random

class Connect4Game:
    def __init__(self, player1, player2):
        # Initialize game state
        self.player1 = player1
        self.player2 = player2
        self.current_player_index = 0  # Index of current player in the players list
        self.players = [player1, player2]
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
                current_piece = self.settings.users[self.players[self.current_player_index]]['piece']
                self.board[i][column] = current_piece
                if self.check_winner(current_piece, i, column):  # Check for a winner
                    print(f"Player {self.players[self.current_player_index]} wins!")
                    self.display_board()  # Show the board with the winning move
                    return True
                if self.check_draw():  # Check for a draw
                    print("The game is a draw!")
                    return True
                return False  # Successfully dropped piece without ending the game
        print("Column is full. Please choose another column.")
        return False
    
    def check_winner(self, piece, row, col):
        # Check for four consecutive pieces in a row
        print("Checking row...")
        if col <= 3 and all(self.board[row][col + i] == piece for i in range(4)):
            print("Winning sequence in row")
            return True
            
        # Check for four consecutive pieces in a column
        print("Checking column...")
        if row <= 2 and all(self.board[row + i][col] == piece for i in range(4)):
            print("Winning sequence in column")
            return True
            
        # Check for four consecutive pieces in a diagonal (down-right)
        print("Checking diagonal (down-right)...")
        if row <= 2 and col <= 3 and all(self.board[row + i][col + i] == piece for i in range(4)):
            print("Winning sequence in diagonal (down-right)")
            return True
            
        # Check for four consecutive pieces in a diagonal (down-left)
        print("Checking diagonal (down-left)...")
        if row <= 2 and col >= 3 and all(self.board[row + i][col - i] == piece for i in range(4)):
            print("Winning sequence in diagonal (down-left)")
            return True
            
        return False
    
    def check_draw(self):
        # Check if the board is full (no empty spaces)
        return all(cell != ' ' for row in self.board for cell in row)
    
    def restart_game(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player_index = random.randint(0, 1)  # Random player

    def play(self):
        while True:
            print("DEBUG: Current player before turn:", self.players[self.current_player_index])
            self.display_board()
            while True:
                column = input(f"Player {self.players[self.current_player_index]}, enter column number to drop piece: ")
                if column.isdigit():
                    column = int(column)
                    if 1 <= column <= 7:
                        break
                print("Invalid input. Please enter a number between 1 and 7.")
            if self.drop_piece(column):
                print("DEBUG: Current player after successful turn:", self.players[self.current_player_index])
                last_row = 0  # Initialize last row to 0
                for row in range(6):
                    if self.board[row][column - 1] != ' ':
                        last_row = row  # Update last row if piece is found
                if self.check_winner(self.settings.users[self.players[self.current_player_index]]['piece'], last_row, column - 1):
                    print(f"Player {self.players[self.current_player_index]} wins!")
                elif self.check_draw():
                    print("The game is a draw!")
                if input("Do you want to play again? (yes/no): ").lower() != "yes":
                    break
                self.restart_game()
            # Toggle between players
            self.current_player_index = (self.current_player_index + 1) % 2
            print("DEBUG: Current player after turn:", self.players[self.current_player_index])


# Run the game
if __name__ == "__main__":
    game = Connect4Game("Player 1", "Player 2")
    game.play()