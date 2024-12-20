import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color: str, center_init_pos: int) -> None:
        super().__init__()

        self._color: str = color
        self._image: pygame.surface.Surface = None

        self.value: int = 0 # 1 for red -1 for yellow

        if color == "red":
            self._image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_red.png").convert_alpha()
            self.value = 1
        elif color == "yellow":
            self._image: pygame.surface.Surface = pygame.image.load(r"Assets\coin_yellow.png").convert_alpha()
            self.value = -1

        self._rect: pygame.rect.Rect = self._image.get_rect()
        self._rect.centery: int = center_init_pos

        # Falling variables
        self._vert_speed: int = 0
        

    def set_centerx_to(self, pos_x: int) -> None:
        self._rect.centerx = pos_x


    def animation_fall(self, centerx: int) -> None:
        self._rect.centerx = centerx

        self._rect.centery += self._vert_speed
        self._vert_speed += 1


    def set_coin_bottom(self, value: int) -> int:
        self._rect.bottom = value


    def get_coin_bottom(self) -> int:
        return self._rect.bottom


    def get_coin_height(self) -> int:
        return self._rect.height


    def get_image(self) -> pygame.surface.Surface:
        return self._image


    def reset_pos(self) -> None:
        self._rect.top = 0
        self._vert_speed = 0


    def draw(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self._image, self._rect)