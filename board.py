import pygame

class Board:
    def __init__(self, board_size_y=7, board_size_x=6) -> None:
        self.board = []
        self.board_size_y = board_size_y
        self.board_size_x = board_size_x

    
    def create(self) -> None:
        # Create a nested 2D list:
        # Amount columns = board_size_x, Amount rows = board_size_y

        for _ in range(self.board_size_x):
            self.board.append(self.board_size_y * [0])