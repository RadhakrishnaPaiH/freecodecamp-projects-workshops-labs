from abc import ABC, abstractmethod
import random


# Abstract base class
class Player(ABC):

    def __init__(self):
        # List of possible moves.
        # Concrete classes (like Pawn) will define these.
        self.moves = []

        # Starting position on the board
        self.position = (0, 0)

        # Track every position visited.
        # Starts with the initial position.
        self.path = [self.position]

    def make_move(self):
        # Choose a random move from the available moves
        move = random.choice(self.moves)

        # Update the current position by adding
        # the move coordinates to the current coordinates
        self.position = (
            self.position[0] + move[0],  # x-coordinate
            self.position[1] + move[1]   # y-coordinate
        )

        # Store the new position in the path history
        self.path.append(self.position)

        # Return the updated position
        return self.position

    # Abstract method that every subclass must implement
    @abstractmethod
    def level_up(self):
        pass


# Concrete Player class
class Pawn(Player):

    def __init__(self):
        # Initialize attributes from Player
        super().__init__()

        # Basic Pawn moves:
        # up, down, left, right
        self.moves = [
            (0, 1),   # move up
            (0, -1),  # move down
            (-1, 0),  # move left
            (1, 0)    # move right
        ]

    def level_up(self):
        # Add diagonal movements when the Pawn levels up
        self.moves.extend([
            (-1, 1),   # up-left
            (1, 1),    # up-right
            (-1, -1),  # down-left
            (1, -1)    # down-right
        ])
