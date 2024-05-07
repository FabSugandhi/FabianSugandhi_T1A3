# player.py
'''
Module to define the player class
'''
class Player:
    def __init__(self, name, piece, color):
        self.name = name
        self.piece = piece
        self.color = color
        self.match_history = []

    def add_match_record(self, opponent, result):
        self.match_history.append({'opponent': opponent, 'result': result})

    def __str__(self):
        return f"{self.name}: {self.piece} ({self.color})"

if __name__ == "__main__":
    player1 = Player("Player 1", "X", "Red")
    player2 = Player("Player 2", "O", "Yellow")
    player1.add_match_record("Player 2", "Win")
    player1.add_match_record("Player 3", "Loss")
    print(player1.match_history)