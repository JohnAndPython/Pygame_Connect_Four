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



board_1 = Board()
centersx = board_1.get_centersx()

player_yel = Player("yellow", 50)
player_red = Player("red", 60)

# Selection bar
select_bar = dict()
select_left = 0
for index in range(7):
    select_bar[index] = pygame.rect.Rect(0, 0, 20, 120)
    select_bar[index].centerx = centersx[index]







main_board = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 0, 0],
              [0, 0, 1, -1, -1, 0, 0],
              [0, 0, -1, 1, 1, 0, 0],
              [0, -1, 1, 1, 1, 1, 0]]

left = 15
top = 15
circle_size = (80, 80)

# Nested List for coins
# [color, circle_size]
circles = []

for _ in range(6):
    circles.append(7 * [0])


# Coin colors
white = (255, 255, 255)
yellow = (200, 200, 0)
red = (200, 0, 0)


# Chnage values of list circles based on the values in the nested list main_board
for ind_row, row in enumerate(main_board):
    for ind_col, value in enumerate(row):
        if value == 0:
            circles[ind_row][ind_col] = (white, (left, top, *circle_size))
        elif value == -1:
            circles[ind_row][ind_col] = (red, (left, top, *circle_size))
        elif value == 1:
            circles[ind_row][ind_col] = (yellow, (left, top, *circle_size))

        left += 90

    top += 90
    left = 15


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




    screen.fill((255, 255, 255))

    
    player_red.set_centerx_to(m_pos[0])
    player_red.draw(screen)
    board_1.draw(screen)


    for key, field in select_bar.items():
        pygame.draw.rect(screen, (250, 0, 0), field)
        

        if field.collidepoint(m_pos):
            #print(circles[0][key][1][0])
            posx = circles[0][key][1][0]
            posy = posx + 80
            pygame.draw.line(screen, (0, 200, 150), (posx +10 , 140), (posy +10, 140), 10)


    pygame.display.flip()

    #set max FPS to 60
    clock.tick(60)