import pygame
import time
import sys

from board import Board

pygame.init()

SCREEN_WIDTH = 674
SCREEN_HEIGHT = 730

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

prev_time = time.time()


dot_surf = pygame.surface.Surface((80, 80))
dot_rect = dot_surf.get_rect()
dot_rect.top = 50

b_surf = pygame.surface.Surface((650, 560))
b_rect = b_surf.get_rect()
b_rect.left = 12
b_rect.top = 150

main_board = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 0, 0],
              [0, 0, 1, -1, -1, 0, 0],
              [0, 0, -1, 1, 1, 0, 0],
              [0, -1, 1, 1, 1, 1, 0]]

left = 15
top = 15
circle_size = (80, 80)

circles = []

for _ in range(6):
    circles.append(7 * [0])



white = (255, 255, 255)
yellow = (200, 200, 0)
red = (200, 0, 0)


for ind_row, row in enumerate(main_board):
    for ind_col, value in enumerate(row):
        if value == 0:
            circles[ind_row][ind_col] = (b_surf, white, (left, top, *circle_size))
        elif value == -1:
            circles[ind_row][ind_col] = (b_surf, red, (left, top, *circle_size))
        elif value == 1:
            circles[ind_row][ind_col] = (b_surf, yellow, (left, top, *circle_size))

        left += 90

    top += 90
    left = 15


print(circles)


# for _ in range(7):
#     circles.append((b_surf, (255, 255, 255), (left, 10, 100, 100)))
#     left += 140


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
    b_surf.fill((0, 0, 230))
    

    for row in circles:
        for value in row:
            pygame.draw.ellipse(*value)

    screen.blit(b_surf, b_rect)

    dot_rect.centerx = m_pos[0]
    pygame.draw.ellipse(screen, (0, 0, 0), dot_rect)

    


    # for circle in circles:
    #     pygame.draw.ellipse(*circle)

        

    


    #update display
    #pygame.display.update()
    pygame.display.flip()

    #set max FPS to 60
    clock.tick(60)