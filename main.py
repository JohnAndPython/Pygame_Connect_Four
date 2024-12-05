import pygame
import time
import sys

from board import Board
from player import Player

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev_time = time.time()

board_1 = Board(lowest_border=SCREEN_HEIGHT)
centersx = board_1.get_centersx()
points_pos = board_1.get_points_pos()

print(board_1._board)
print(board_1._low_border)


player_yel = Player("yellow", 50)
player_red = Player("red", 60)




# Selection bar
select_bar = dict()
select_left = 0
for index in range(7):
    select_bar[index] = pygame.rect.Rect(0, 0, 40, SCREEN_HEIGHT)
    select_bar[index].centerx = centersx[index]


green = (0, 200, 150)
red = (200, 0, 0)
col = (0, 0, 0)
collision = False
index_column = 0



# *************************** Delete ***********************************************

main_board = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 0, 0],
              [0, 0, 1, -1, -1, 0, 0],
              [0, 0, -1, 1, 1, 0, 0],
              [0, -1, 1, 1, 1, 1, 0]]


# *************************** Delete ***********************************************

left = 15
top = 15
circle_size = (80, 80)

# Nested List for coins
# [color, circle_size]
circles = []

for _ in range(6):
    circles.append(7 * [0])

# *************************** Delete ***********************************************
# # Coin colors
# white = (255, 255, 255)
# yellow = (200, 200, 0)
# red = (200, 0, 0)


# # Chnage values of list circles based on the values in the nested list main_board
# for ind_row, row in enumerate(main_board):
#     for ind_col, value in enumerate(row):
#         if value == 0:
#             circles[ind_row][ind_col] = (white, (left, top, *circle_size))
#         elif value == -1:
#             circles[ind_row][ind_col] = (red, (left, top, *circle_size))
#         elif value == 1:
#             circles[ind_row][ind_col] = (yellow, (left, top, *circle_size))

#         left += 90

#     top += 90
#     left = 15
player_clicked = False

while True:
    #delta time |alternative: dt = clock.tick(60) / 1000
    dt = time.time() - prev_time
    prev_time = time.time()

    m_pos = pygame.mouse.get_pos()
    pygame.display.set_caption(f"{m_pos}")

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for index, field in select_bar.items():
                
                if field.collidepoint(m_pos) and not board_1.col_full(index):

                    player_clicked = True
                    index_column = index




    screen.fill((255, 255, 255))



    if player_clicked:
        player_red.animation_fall(centersx[index_column])
        cur_low_border = board_1.get_low_border(index_column)

        if player_red.get_coin_bottom() >= cur_low_border:
            player_red.set_coin_bottom(cur_low_border)

            cur_low_border -= player_red.get_coin_height()
            board_1.set_low_border(index_column, cur_low_border)

            board_1.set_value(index_column, player_red.value)
            print(player_red.value)
            print(board_1._board)
            player_clicked = False

    else:
        player_red.set_centerx_to(m_pos[0])
        for key, field in select_bar.items():
            if field.collidepoint(m_pos) and not board_1.col_full(key):
                 pygame.draw.line(screen, green, *points_pos[key], 10)
                
            elif field.collidepoint(m_pos) and board_1.col_full(key):
                pygame.draw.line(screen, red, *points_pos[key], 10)

           

    #print(collision, index_bar)
    
    player_red.draw(screen)
    board_1.draw(screen)





    pygame.display.flip()

    #set max FPS to 60
    clock.tick(60)