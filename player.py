import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color: str, center_init_pos) -> None:
        super().__init__()

        self._color: str = color
        self.image: pygame.surface.Surface = None

        self._turn: bool = False


        if color == "red":
            self.image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_red.png")
        elif color == "yellow":
            self.image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_yellow.png")

        self.rect = self.image.get_rect()
        self.rect.centery = center_init_pos

    def set_centerx_to(self, pos_x: int) -> None:
        self.rect.centerx = pos_x


    def draw(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self.image, self.rect)