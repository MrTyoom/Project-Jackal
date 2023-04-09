import pygame

WIDTH = 1200
HEIGHT = 720
FPS = 60

FIELD_SIZE_X, FIELD_SIZE_Y = 50, 50

PAUSE_BUTTON_IMAGE = pygame.image.load('images/dark_pause_button.png')
MICRO_BUTTON_IMAGE = pygame.image.load('images/micro_button.png')
MICRO_BUTTON_DARK_IMAGE = pygame.image.load('images/micro_button_dark.png')
PAUSE_BUTTON_DARK_IMAGE = pygame.image.load('images/pause_button_dark.png')


MENU_BACKGROUND = pygame.image.load('images/imgonline-com-ua-Resize-YdYZEYMJxXnKdJx1.jpg')
SHIP_IMAGE = pygame.image.load('images/black_ship.jpg')
CLOSED_FIELD_TILE = pygame.image.load('images/field_jackal.png')

PIRATE_1 = pygame.image.load('images/pirate1.png')
PIRATE_2 = pygame.image.load('images/pirate2.png')
PIRATE_3 = pygame.image.load('images/pirate3.png')
PIRATE_4 = pygame.image.load('images/pirate4.png')
PIRATE_5 = pygame.image.load('images/pirate5.png')
PIRATE_6 = pygame.image.load('images/pirate6.png')

COIN = pygame.image.load('images/coin.png')
ROM = pygame.image.load('images/bottle_rom.png')


# START_BUTTON_IMAGE = pygame.image.load('images/start_button.png')
# QUIT_BUTTON_IMAGE = pygame.image.load('images/quit_button.png').convert_alpha()
# OPTIONS_BUTTON_IMAGE = pygame.image.load('images/options_button.png').convert_alpha()


# 'x' - closed tile, 'o' - opened tile, '-' - ocean, 's' - ship
WORLD_MAP = [
    # 1    2    3    4    5    6    7    8    9    10   11   12   13
    ['-', '-', '-', '-', '-', '-', 'S2', '-', '-', '-', '-', '-', '-'],   # 1
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
    ['-', '-', '-', '-', '-', '-', 'S1', '-', '-', '-', '-', '-', '-'],   # 13
    ]

CODES_TO_INTENTS = ['move_ship_left', 'move_ship_right', 'nothing']

CLICKED_BUTTON = {
    MICRO_BUTTON_IMAGE: MICRO_BUTTON_DARK_IMAGE,
    PAUSE_BUTTON_IMAGE: PAUSE_BUTTON_DARK_IMAGE
}
