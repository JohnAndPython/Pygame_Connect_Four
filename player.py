import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color: str, center_init_pos: int) -> None:
        super().__init__()

        self._color: str = color
        self._image: pygame.surface.Surface = None

        self._turn: bool = False


        if color == "red":
            self._image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_red.png").convert_alpha()
        elif color == "yellow":
            self._image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_yellow.png").convert_alpha()

        self._rect: pygame.rect.Rect = self._image.get_rect()
        self._rect.centery: int = center_init_pos
        
        self._coins: list = []


    def set_centerx_to(self, pos_x: int) -> None:
        self._rect.centerx = pos_x


    def animation_fall(self, centerx) -> None:
        self._rect.centerx = centerx
        self._rect.centery += 5


    def draw(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self._image, self._rect)