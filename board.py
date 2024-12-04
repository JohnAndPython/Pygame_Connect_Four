import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, board_size_y: int=7, board_size_x: int=6) -> None:
        super().__init__()

        self.board: list = []
        self.board_rects: list = []
        self.board_size_y: int = board_size_y
        self.board_size_x : int= board_size_x

        self.image: pygame.surface.Surface = pygame.image.load(r"Assets\board.png")
        self.rect: pygame.rect.Rect = self.image.get_rect()

        # Fill nested 2D List with Pygame rectangles
        left_pos: int = 0
        top_pos: int = 120
        temp_lst: list = []

        for _ in range(self.board_size_x):
            for _ in range(self.board_size_y):
                temp_lst.append(self.image.get_rect(left=left_pos, top=top_pos))
                left_pos += 100

            self.board_rects.append(temp_lst)
            temp_lst = []
            left_pos = 0
            top_pos += 100


    def get_centersx(self) -> list[int]:
        ''' Return a list with the centerx value of each rect in the first row of self.board_rects'''

        return [rect.centerx for rect in self.board_rects[0]]
    

    def get_points_pos(self, offset_width: int=10, offset_height: int=8) -> list[tuple]:
        ''' Create a list of points. The points are the topleft and topright coordinates of the rects in self.board_rects'''
        
        points = []
        pointx_1, pointy_1, pointx_2, pointy_2 = 0, 0, 0, 0
         
        for rect in self.board_rects[0]:
            pointx_1 = rect.topleft[0] + offset_width
            pointy_1 = rect.topleft[1] - offset_height
            pointx_2 = rect.topright[0] - offset_width
            pointy_2 = rect.topright[1] - offset_height

            points.append(((pointx_1, pointy_1), (pointx_2, pointy_2)))

        return points


    def create(self) -> None:
        ''' Create a nested 2D list:
        Amount columns = board_size_x, Amount rows = board_size_y '''

        for _ in range(self.board_size_x):
            self.board.append(self.board_size_y * [0])




    def draw(self, surface: pygame.surface.Surface) -> None:
        ''' Draw the rectangles of the nested list self.board_rects on surface'''
        for row in self.board_rects:
            for rect in row:
                surface.blit(self.image, rect)