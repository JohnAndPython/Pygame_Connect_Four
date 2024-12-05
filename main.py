import pygame
import sys, random

from board import Board
from player import Player

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Init Board and player
board_1 = Board(lowest_border=SCREEN_HEIGHT)
centersx = board_1.get_centersx()
points_pos = board_1.get_points_pos()

player_red = Player("red", 60)
player_yel = Player("yellow", 60)

board_1.config(player_red.get_image(), player_yel.get_image())

# Choose the starting player randomly
cur_player = random.choice([player_red, player_yel])

# Selection bar
select_bar = dict()
select_left = 0
for index in range(7):
    select_bar[index] = pygame.rect.Rect(0, 0, 40, SCREEN_HEIGHT)
    select_bar[index].centerx = centersx[index]

# Colors for line indicators
green = (0, 200, 150)
red = (200, 0, 0)
col = (0, 0, 0)


index_column = 0
player_clicked = False
game_over = False

# Game loop
while True:

    m_pos = pygame.mouse.get_pos()
    pygame.display.set_caption("Connect Four")

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        elif not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            for index, field in select_bar.items():
                if field.collidepoint(m_pos) and not board_1.col_full(index):

                    player_clicked = True
                    index_column = index


    screen.fill((255, 255, 255))


    # Game logic
    if player_clicked:
        cur_player.animation_fall(centersx[index_column])
        cur_low_border = board_1.get_low_border(index_column)

        if cur_player.get_coin_bottom() >= cur_low_border:
            cur_player.set_coin_bottom(cur_low_border)

            cur_low_border -= cur_player.get_coin_height()
            board_1.set_low_border(index_column, cur_low_border)
            board_1.set_value(index_column, cur_player.value)

            ply_value = board_1.check_winner()

            if ply_value == 4:

                game_over = True
            elif ply_value == -4:

                game_over = True

            cur_player.reset_pos()

            if cur_player == player_yel:
                cur_player = player_red
            elif cur_player == player_red:
                cur_player = player_yel
            
            player_clicked = False

    elif not game_over:
        cur_player.set_centerx_to(m_pos[0])
        for key, field in select_bar.items():
            if field.collidepoint(m_pos) and not board_1.col_full(key):
                 pygame.draw.line(screen, green, *points_pos[key], 10)
                
            elif field.collidepoint(m_pos) and board_1.col_full(key):
                pygame.draw.line(screen, red, *points_pos[key], 10)

           
    # Draw coins and board
    if not game_over:
        cur_player.draw(screen)

    board_1.draw_coins(screen)
    board_1.draw(screen)
    
    # Update screen
    pygame.display.flip()

    #set max FPS to 60
    clock.tick(60)