import pygame

WIDTH = 1200
HEIGHT = 720
FPS = 60


FIELD_SIZE_X, FIELD_SIZE_Y = 50, 50
PAUSE_BUTTON_IMAGE = pygame.image.load('images/dark_pause_button.png')
MICRO_BUTTON_IMAGE = pygame.image.load('images/micro_button.png')
MENU_BACKGROUND = pygame.image.load('images/imgonline-com-ua-Resize-YdYZEYMJxXnKdJx1.jpg')
SHIP_IMAGE = pygame.image.load('images/black_ship.jpg')
CLOSED_FIELD_TILE = pygame.image.load('images/field_jackal.png')
# START_BUTTON_IMAGE = pygame.image.load('images/start_button.png')
# QUIT_BUTTON_IMAGE = pygame.image.load('images/quit_button.png').convert_alpha()
# OPTIONS_BUTTON_IMAGE = pygame.image.load('images/options_button.png').convert_alpha()


# 'x' - closed tile, 'o' - opened tile, '-' - ocean, 's' - ship
WORLD_MAP = [
    # 1    2    3    4    5    6    7    8    9    10   11   12   13
    ['-', '-', '-', '-', '-', '-', 'S', '-', '-', '-', '-', '-', '-'],   # 1
    ['-', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', '-'],   # 2
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 3
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 4
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 5
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 6
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 7
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 8
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 9
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 10
    ['-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-'],   # 11
    ['-', '-', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '-', '-'],   # 12
    ['-', '-', '-', '-', '-', '-', 'S', '-', '-', '-', '-', '-', '-'],   # 13
    ]



