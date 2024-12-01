import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self._color = color

        self._turn = False