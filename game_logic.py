import random

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        # Implement logic to add a random tile to the board
        pass

    def move(self, direction):
        # Implement logic to move tiles in the specified direction
        pass

    def is_game_over(self):
        # Implement logic to check if the game is over
        pass