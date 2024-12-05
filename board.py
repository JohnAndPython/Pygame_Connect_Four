import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, board_size_y: int=6, board_size_x: int=7, lowest_border: int=0) -> None:
        super().__init__()

        self._board: list = []
        self._board_size_y: int = board_size_y
        self._board_size_x: int= board_size_x
        self._lowest_border: int = lowest_border

        for _ in range(self._board_size_y):
            self._board.append(self._board_size_x * [0])

        self._board_rects: list = []

        self._image: pygame.surface.Surface = pygame.image.load(r"Assets\board.png").convert_alpha()
        self._rect: pygame.rect.Rect = self._image.get_rect()

        # Fill nested 2D List with Pygame rectangles
        left_pos: int = 0
        top_pos: int = 120
        temp_lst: list = []

        for _ in range(self._board_size_y):
            for _ in range(self._board_size_x):
                temp_lst.append(self._image.get_rect(left=left_pos, top=top_pos))
                left_pos += 100

            self._board_rects.append(temp_lst)
            temp_lst = []
            left_pos = 0
            top_pos += 100


        self._low_border: list = [self._lowest_border] * self._board_size_x

        # Player variables
        self._ply_image_1: pygame.surface.Surface = None
        self._ply_image_2: pygame.surface.Surface = None


    def config(self, ply_image_1: pygame.surface.Surface, ply_image_2: pygame.surface.Surface) -> None:
        self._ply_image_1 = ply_image_1
        self._ply_image_2 = ply_image_2

    
    def get_centersx(self) -> list[int]:
        ''' Return a list with the centerx value of each rect in the first row of self.board_rects'''

        return [rect.centerx for rect in self._board_rects[0]]
    

    def get_points_pos(self, offset_width: int=10, offset_height: int=8) -> list[tuple]:
        ''' Create a list of points. The points are the topleft and topright coordinates of the rects in self.board_rects'''
        
        points = []
        pointx_1, pointy_1, pointx_2, pointy_2 = 0, 0, 0, 0
         
        for rect in self._board_rects[0]:
            pointx_1 = rect.topleft[0] + offset_width
            pointy_1 = rect.topleft[1] - offset_height
            pointx_2 = rect.topright[0] - offset_width
            pointy_2 = rect.topright[1] - offset_height

            points.append(((pointx_1, pointy_1), (pointx_2, pointy_2)))

        return points


    def col_full(self, index: int) -> bool:
        ''' Check if a column is full or not. Full = Column is completly filled with values other than zeros'''

        if self._board[0][index] != 0:
            return True
        else:
            return False


    def set_low_border(self, index: int, value: int) -> None:
        self._low_border[index] = value


    def get_low_border(self, index: int) -> int:
        return self._low_border[index]
    

    def set_value(self, index: int, value: int) -> None:

        for ind, row in enumerate(self._board):
            if row[index] == 0 and ind == self._board_size_y - 1:
                self._board[ind][index] = value
            elif row[index] != 0:
                self._board[ind-1][index] = value
                break


    def check_winner(self) -> int:

        # Check horizontal
        for row in range(len(self._board)):
            for col in range(len(self._board[0])- 3):
                sum_horizontal = sum(self._board[row][col:col + 4])

                if sum_horizontal == 4:
                    return 4
                
                if sum_horizontal == -4:
                    return -4
                

        # Check Vertical
        lst_vertical = []   
        for col in range(0, len(self._board)):
            for row in range(0, len(self._board)-3):
                lst_vertical.append(self._board[row][col])
                lst_vertical.append(self._board[row + 1][col])
                lst_vertical.append(self._board[row + 2][col])
                lst_vertical.append(self._board[row + 3][col])
                sum_vertical = sum(lst_vertical)

                if sum_vertical == 4:
                    return 4
                if sum_vertical == -4:
                    return -4
                
                lst_vertical.clear()


        # Check diagonal left to right
        lst_diagonalLR = []
        for col in range(0, len(self._board[0]) - 3):
            for row in range(0, len(self._board) - 3):
                lst_diagonalLR.append(self._board[row][col])
                lst_diagonalLR.append(self._board[row + 1][col + 1])
                lst_diagonalLR.append(self._board[row + 2][col + 2])
                lst_diagonalLR.append(self._board[row + 3][col + 3])
                sum_diagonal_lr = sum(lst_diagonalLR)

                if sum_diagonal_lr == 4:
                    return 4
                elif sum_diagonal_lr == -4:
                    return -4
                
                lst_diagonalLR.clear()

        
        # Check diagonal right to left
        lst_diagonalRL = []
        for col in range(len(self._board[0])-1, len(self._board[0])- 5, -1):
            for row in range(0, len(self._board) - 3):
                lst_diagonalRL.append(self._board[row][col])
                lst_diagonalRL.append(self._board[row + 1][col - 1])
                lst_diagonalRL.append(self._board[row + 2][col - 2])
                lst_diagonalRL.append(self._board[row + 3][col - 3])
                sum_diagonal_rl = sum(lst_diagonalRL)

                if sum_diagonal_rl == 4:
                    return 4
                elif sum_diagonal_rl == -4:
                    return -4
                
                lst_diagonalRL.clear()

        return 0


    def reset(self) -> None:
        ''' reset all values '''

        self._board: list = []

        for _ in range(self._board_size_y):
            self._board.append(self._board_size_x * [0])

        self._low_border: list = [self._lowest_border] * self._board_size_x


    def draw(self, surface: pygame.surface.Surface) -> None:
        ''' Draw the rectangles of the nested list self.board_rects on surface'''

        for row in self._board_rects:
            for rect in row:
                surface.blit(self._image, rect)


    def draw_coins(self, surface: pygame.surface.Surface) -> None:
        ''' Draw all played coins'''

        for ind_row, row in enumerate(self._board):
            for ind_col, value in enumerate(row):
                if value == 1:
                    surface.blit(self._ply_image_1, self._board_rects[ind_row][ind_col])
                elif value == -1:
                    surface.blit(self._ply_image_2, self._board_rects[ind_row][ind_col])