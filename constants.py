from buttons import *
from random import shuffle
from collections import namedtuple
import queue

WIDTH = 1440
HEIGHT = 770
FPS = 60
MOVE = 1
TMP = 1
MY_FONT = pygame.font.match_font('islandmomentsregular')

FIELD_SIZE_X, FIELD_SIZE_Y = 55, 55

SHIP1_COORD = {
    'x': 6,
    'y': 12
}
SHIP2_COORD = {
    'x': 6,
    'y': 0
}

MENU_BACKGROUND = pygame.transform.scale(pygame.image.load('images/menu_background.jpg'), (WIDTH, HEIGHT))
PAUSE_BACKGROUND = pygame.transform.scale(pygame.image.load('images/pause_background.png'), (WIDTH / 2, HEIGHT / 2))
RODGER = pygame.transform.scale(pygame.image.load('images/rodger.png'), (WIDTH / 8, HEIGHT / 8))

# numbers in arrow names mean number of quarter on a trigonometric circle
ARROW_RIGHT_TILE = pygame.image.load('images/field_tiles/arrow_right.png')                                              # 1
ARROW_RIGHT_LEFT_TILE = pygame.image.load('images/field_tiles/arrow_right_left.png')                                    # 2
ARROW_RIGHT_DIAGONAL1_TILE = pygame.image.load('images/field_tiles/arrow_right-diagonal(45).png')                       # 3
ARROW_RIGHT_LEFT_DIAGONAL_1_TILE = pygame.image.load('images/field_tiles/arrow_right-left-diagonal(45).png')            # 4
ARROW_UP_DOWN_RIGHT_LEFT_TILE = pygame.image.load('images/field_tiles/arrow_up-down-right-left.png')                    # 5
ARROW_UP_DOWN_RIGHT_LEFT_DIAGONAL_TILE = pygame.image.load('images/field_tiles/arrow_up-down-right-left-diagonal.png')  # 6
ARROW_LEFT_DIAGONAL4_ARROW_RIGHT_DOWN_TILE = pygame.image.load('images/field_tiles/arrow_diagonal(135)_arrow_up_down.png') # 7

BALLOON_TILE = pygame.image.load('images/field_tiles/balloon_tile.png')               # 8
BARREL_TILE = pygame.image.load('images/field_tiles/barrel_tile.png')                 # 9
CANNIBAL_TILE = pygame.image.load('images/field_tiles/cannibal_tile.png')             # 10
CASTLE_TILE = pygame.image.load('images/field_tiles/camp_tile.png')                   # 11
CASTLE_GIRL_TILE = pygame.image.load('images/field_tiles/camp_girl_tile.png')         # 12
CLOSED_FIELD_TILE = pygame.image.load('images/field_tiles/closed_field_tile.png')     # 100
CROC_TILE = pygame.image.load('images/field_tiles/croc_tile.png')                     # 13
GOLD_1_TILE = pygame.image.load('images/field_tiles/gold_1_tile.png')                 # 14
GOLD_2_TILE = pygame.image.load('images/field_tiles/gold_2_tile.png')                 # 15
GOLD_3_TILE = pygame.image.load('images/field_tiles/gold_3_tile.png')                 # 16
GOLD_4_TILE = pygame.image.load('images/field_tiles/gold_4_tile.png')                 # 17
GOLD_5_TILE = pygame.image.load('images/field_tiles/gold_5_tile.png')                 # 18
HORSE_TILE = pygame.image.load('images/field_tiles/horse_tile.png')                   # 19
ICE_TILE = pygame.image.load('images/field_tiles/ice_tile.png')                       # 20
LABYRINTH_2_TILE = pygame.image.load('images/field_tiles/labyrinth_2_tile.png')       # 21
LABYRINTH_3_TILE = pygame.image.load('images/field_tiles/labyrinth_3_tile.png')       # 22
LABYRINTH_4_TILE = pygame.image.load('images/field_tiles/labyrinth_4_tile.png')       # 23
LABYRINTH_5_TILE = pygame.image.load('images/field_tiles/labyrinth_5_tile.png')       # 24
NOTHING_1_TILE = pygame.image.load('images/field_tiles/nothing_1.png')                # 25
NOTHING_2_TILE = pygame.image.load('images/field_tiles/nothing_2.png')                # 26
NOTHING_3_TILE = pygame.image.load('images/field_tiles/nothing_3.png')                # 27
NOTHING_4_TILE = pygame.image.load('images/field_tiles/nothing_4.png')                # 28
PLANE_TILE = pygame.image.load('images/field_tiles/plane_tile.png')                   # 29
SHIP_IMAGE = pygame.image.load('images/field_tiles/black_ship.jpg')                   # 101
TRAP_TILE = pygame.image.load('images/field_tiles/trap_tile.png')                     # 30
CANNON_TILE = pygame.image.load('images/field_tiles/cannon_tile.png')                 # 31
WHITE_TILE = pygame.image.load('images/field_tiles/white_tile.png')                   # 32


PIRATE_1 = pygame.image.load('images/pirate1.png')
W1, H1 = PIRATE_1.get_width(), PIRATE_1.get_height()
PIRATE_2 = pygame.image.load('images/pirate2.png')
W2, H2 = PIRATE_2.get_width(), PIRATE_2.get_height()
PIRATE_3 = pygame.image.load('images/pirate3.png')
W3, H3 = PIRATE_3.get_width(), PIRATE_3.get_height()
PIRATE_4 = pygame.image.load('images/pirate4.png')
W4, H4 = PIRATE_4.get_width(), PIRATE_4.get_height()
PIRATE_5 = pygame.image.load('images/pirate5.png')
W5, H5 = PIRATE_5.get_width(), PIRATE_5.get_height()
PIRATE_6 = pygame.image.load('images/pirate6.png')
W6, H6 = PIRATE_6.get_width(), PIRATE_6.get_height()
DEAD_PIRATE_1 = pygame.image.load('images/pirate1_dead.png')
DEAD_PIRATE_2 = pygame.image.load('images/pirate2_dead.png')
DEAD_PIRATE_3 = pygame.image.load('images/pirate3_dead.png')
DEAD_PIRATE_4 = pygame.image.load('images/pirate4_dead.png')
DEAD_PIRATE_5 = pygame.image.load('images/pirate5_dead.png')
DEAD_PIRATE_6 = pygame.image.load('images/pirate6_dead.png')


COIN = pygame.image.load('images/coin.png')


CODE_TO_TILE = {1: ARROW_RIGHT_TILE,                           # +
                2: ARROW_RIGHT_LEFT_TILE,                      # +
                3: ARROW_RIGHT_DIAGONAL1_TILE,                 # +
                4: ARROW_RIGHT_LEFT_DIAGONAL_1_TILE,           # +
                5: ARROW_UP_DOWN_RIGHT_LEFT_TILE,              # +
                6: ARROW_LEFT_DIAGONAL4_ARROW_RIGHT_DOWN_TILE, # +
                7: ARROW_UP_DOWN_RIGHT_LEFT_DIAGONAL_TILE,     # +
                8: BALLOON_TILE,       # +
                9: BARREL_TILE,        # +
                10: CANNIBAL_TILE,     # +
                11: CASTLE_TILE,       # +
                12: CASTLE_GIRL_TILE,  # +
                13: CROC_TILE,         # +
                14: GOLD_1_TILE,       # +
                15: GOLD_2_TILE,       # +
                16: GOLD_3_TILE,       # +
                17: GOLD_4_TILE,       # +
                18: GOLD_5_TILE,       # +
                19: HORSE_TILE,        # +
                20: ICE_TILE,
                21: LABYRINTH_2_TILE,  # +      little troubles, because i don't understand how to count moves
                22: LABYRINTH_3_TILE,  # +
                23: LABYRINTH_4_TILE,  # +
                24: LABYRINTH_5_TILE,  # +
                25: NOTHING_1_TILE,    # +
                26: NOTHING_2_TILE,    # +
                27: NOTHING_3_TILE,    # +
                28: NOTHING_4_TILE,    # +
                29: PLANE_TILE,
                30: TRAP_TILE,         # +
                31: CANNON_TILE,       # +
                100: CLOSED_FIELD_TILE,
                101: SHIP_IMAGE,
                102: SHIP_IMAGE}

EVENTS = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7,
          8, 8, 9, 9, 9, 9, 10, 11, 11, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 15, 15,
          15, 15, 15, 16, 16, 16, 17, 17, 18, 19, 19, 20, 20, 20, 20, 20, 20,
          21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 24, 25, 25, 25, 25, 25,
          25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27,
          27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28,
          28, 29, 30, 30, 30, 31, 31]
shuffle(EVENTS)


WORLD_MAP = [
    #  1         2        3        4        5        6         7         8        9       10       11       12        13
    [Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(102), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0)],                       # 1
    [Tile(0), Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0), Tile(0)],       # 2
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 3
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 4
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 5
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 6
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 7
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 8
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 9
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 10
    [Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0)],   # 11
    [Tile(0), Tile(0), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(100), Tile(0), Tile(0)],       # 12
    [Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(101), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0), Tile(0)],                       # 13
    ]


# WATER_TILES = []
cnt = 0
for i in range(len(WORLD_MAP)):
    for j in range(len(WORLD_MAP[i])):
        WORLD_MAP[i][j].x, WORLD_MAP[i][j].y = j, i
        if WORLD_MAP[i][j].code == 100:
            WORLD_MAP[i][j].code = EVENTS[cnt]
            cnt += 1



CODES_TO_INTENTS = ['move_ship_left', 'move_ship_right', 'nothing']

pirate1 = Pirate(1, 0)
pirate2 = Pirate(1, 1)
pirate3 = Pirate(1, 2)
pirate4 = Pirate(2, 3)
pirate5 = Pirate(2, 4)
pirate6 = Pirate(2, 5)

GLOBAL_PIRATES = {
    0: pirate1,
    1: pirate2,
    2: pirate3,
    3: pirate4,
    4: pirate5,
    5: pirate6
}

Command = namedtuple("Command", "was go pirate")


# a couple of tests


TESTS = [
    Command(WORLD_MAP[12][6], WORLD_MAP[11][6], pirate1),
    Command(WORLD_MAP[0][6], WORLD_MAP[1][6], pirate6),
    Command(WORLD_MAP[11][6], WORLD_MAP[10][6], pirate1),
    Command(WORLD_MAP[1][6], WORLD_MAP[1][5], pirate6),
    Command(WORLD_MAP[12][6], WORLD_MAP[11][6], pirate2),
    Command(WORLD_MAP[0][6], WORLD_MAP[1][6], pirate5),
    Command(WORLD_MAP[12][6], WORLD_MAP[11][6], pirate3),
    Command(WORLD_MAP[0][6], WORLD_MAP[1][6], pirate4),
]

# TESTS = [
#     Command(WORLD_MAP[12][6], WORLD_MAP[11][6], pirate6),  # снизу от корабля до крайней левой клетки поля
#     Command(WORLD_MAP[11][6], WORLD_MAP[11][5], pirate6),
#     Command(WORLD_MAP[11][5], WORLD_MAP[11][4], pirate6),
#     Command(WORLD_MAP[11][4], WORLD_MAP[11][3], pirate6),
#     Command(WORLD_MAP[11][3], WORLD_MAP[11][2], pirate6),
#
#     Command(WORLD_MAP[11][2], WORLD_MAP[10][1], pirate6),  # поднялись на клетку по диагонали вправо
#
#     # ряд 1
#     Command(WORLD_MAP[10][1], WORLD_MAP[9][1], pirate6),  # неполный ряд вверх
#     Command(WORLD_MAP[9][1], WORLD_MAP[8][1], pirate6),
#     Command(WORLD_MAP[8][1], WORLD_MAP[7][1], pirate6),
#     Command(WORLD_MAP[7][1], WORLD_MAP[6][1], pirate6),
#     Command(WORLD_MAP[6][1], WORLD_MAP[5][1], pirate6),
#     Command(WORLD_MAP[5][1], WORLD_MAP[4][1], pirate6),
#     Command(WORLD_MAP[4][1], WORLD_MAP[3][1], pirate6),
#     Command(WORLD_MAP[3][1], WORLD_MAP[2][1], pirate6),
#
#     Command(WORLD_MAP[2][1], WORLD_MAP[1][2], pirate6),  # переход на клетку вверх по диагонали влево
#
#     # ряд 2
#     Command(WORLD_MAP[1][2], WORLD_MAP[2][2], pirate6),  # полный ряд вниз
#     Command(WORLD_MAP[2][2], WORLD_MAP[3][2], pirate6),
#     Command(WORLD_MAP[3][2], WORLD_MAP[4][2], pirate6),
#     Command(WORLD_MAP[4][2], WORLD_MAP[5][2], pirate6),
#     Command(WORLD_MAP[5][2], WORLD_MAP[6][2], pirate6),
#     Command(WORLD_MAP[6][2], WORLD_MAP[7][2], pirate6),
#     Command(WORLD_MAP[7][2], WORLD_MAP[8][2], pirate6),
#     Command(WORLD_MAP[8][2], WORLD_MAP[9][2], pirate6),
#     Command(WORLD_MAP[9][2], WORLD_MAP[10][2], pirate6),
#
#     Command(WORLD_MAP[10][2], WORLD_MAP[10][3], pirate6),  # перестроение снизу на следующий ряд справа
#
#     # ряд 3
#     Command(WORLD_MAP[10][3], WORLD_MAP[9][3], pirate6),  # полный ряд вверх
#     Command(WORLD_MAP[9][3], WORLD_MAP[8][3], pirate6),
#     Command(WORLD_MAP[8][3], WORLD_MAP[7][3], pirate6),
#     Command(WORLD_MAP[7][3], WORLD_MAP[6][3], pirate6),
#     Command(WORLD_MAP[6][3], WORLD_MAP[5][3], pirate6),
#     Command(WORLD_MAP[5][3], WORLD_MAP[4][3], pirate6),
#     Command(WORLD_MAP[4][3], WORLD_MAP[3][3], pirate6),
#     Command(WORLD_MAP[3][3], WORLD_MAP[2][3], pirate6),
#     Command(WORLD_MAP[2][3], WORLD_MAP[1][3], pirate6),
#
#     Command(WORLD_MAP[1][3], WORLD_MAP[1][4], pirate6),  # перестроение сверху на следующий ряд справа
#
#     # ряд 4
#     Command(WORLD_MAP[1][4], WORLD_MAP[2][4], pirate6),  # полный ряд вниз
#     Command(WORLD_MAP[2][4], WORLD_MAP[3][4], pirate6),
#     Command(WORLD_MAP[3][4], WORLD_MAP[4][4], pirate6),
#     Command(WORLD_MAP[4][4], WORLD_MAP[5][4], pirate6),
#     Command(WORLD_MAP[5][4], WORLD_MAP[6][4], pirate6),
#     Command(WORLD_MAP[6][4], WORLD_MAP[7][4], pirate6),
#     Command(WORLD_MAP[7][4], WORLD_MAP[8][4], pirate6),
#     Command(WORLD_MAP[8][4], WORLD_MAP[9][4], pirate6),
#     Command(WORLD_MAP[9][4], WORLD_MAP[10][4], pirate6),
#
#     Command(WORLD_MAP[10][4], WORLD_MAP[10][5], pirate6),  # перестроение снизу на следующий ряд справа
#
#     # ряд 5
#     Command(WORLD_MAP[10][5], WORLD_MAP[9][5], pirate6),  # полный ряд вверх
#     Command(WORLD_MAP[9][5], WORLD_MAP[8][5], pirate6),
#     Command(WORLD_MAP[8][5], WORLD_MAP[7][5], pirate6),
#     Command(WORLD_MAP[7][5], WORLD_MAP[6][5], pirate6),
#     Command(WORLD_MAP[6][5], WORLD_MAP[5][5], pirate6),
#     Command(WORLD_MAP[5][5], WORLD_MAP[4][5], pirate6),
#     Command(WORLD_MAP[4][5], WORLD_MAP[3][5], pirate6),
#     Command(WORLD_MAP[3][5], WORLD_MAP[2][5], pirate6),
#     Command(WORLD_MAP[2][5], WORLD_MAP[1][5], pirate6),
#
#     Command(WORLD_MAP[1][5], WORLD_MAP[1][6], pirate6),  # перестроение сверху на следующий ряд справа
#
#     # ряд 6
#     Command(WORLD_MAP[1][6], WORLD_MAP[2][6], pirate6),  # полный ряд вниз
#     Command(WORLD_MAP[2][6], WORLD_MAP[3][6], pirate6),
#     Command(WORLD_MAP[3][6], WORLD_MAP[4][6], pirate6),
#     Command(WORLD_MAP[4][6], WORLD_MAP[5][6], pirate6),
#     Command(WORLD_MAP[5][6], WORLD_MAP[6][6], pirate6),
#     Command(WORLD_MAP[6][6], WORLD_MAP[7][6], pirate6),
#     Command(WORLD_MAP[7][6], WORLD_MAP[8][6], pirate6),
#     Command(WORLD_MAP[8][6], WORLD_MAP[9][6], pirate6),
#     Command(WORLD_MAP[9][6], WORLD_MAP[10][6], pirate6),
#
#     Command(WORLD_MAP[10][6], WORLD_MAP[10][7], pirate6),  # перестроение снизу на следующий ряд справа
#
#     # ряд 7
#     Command(WORLD_MAP[10][7], WORLD_MAP[9][7], pirate6),  # полный ряд вверх
#     Command(WORLD_MAP[9][7], WORLD_MAP[8][7], pirate6),
#     Command(WORLD_MAP[8][7], WORLD_MAP[7][7], pirate6),
#     Command(WORLD_MAP[7][7], WORLD_MAP[6][7], pirate6),
#     Command(WORLD_MAP[6][7], WORLD_MAP[5][7], pirate6),
#     Command(WORLD_MAP[5][7], WORLD_MAP[4][7], pirate6),
#     Command(WORLD_MAP[4][7], WORLD_MAP[3][7], pirate6),
#     Command(WORLD_MAP[3][7], WORLD_MAP[2][7], pirate6),
#     Command(WORLD_MAP[2][7], WORLD_MAP[1][7], pirate6),
#
#     Command(WORLD_MAP[1][7], WORLD_MAP[1][8], pirate6),  # перестроение сверху на следующий ряд справа
#
#     # ряд 8
#     Command(WORLD_MAP[1][8], WORLD_MAP[2][8], pirate6),  # полный ряд вниз
#     Command(WORLD_MAP[2][8], WORLD_MAP[3][8], pirate6),
#     Command(WORLD_MAP[3][8], WORLD_MAP[4][8], pirate6),
#     Command(WORLD_MAP[4][8], WORLD_MAP[5][8], pirate6),
#     Command(WORLD_MAP[5][8], WORLD_MAP[6][8], pirate6),
#     Command(WORLD_MAP[6][8], WORLD_MAP[7][8], pirate6),
#     Command(WORLD_MAP[7][8], WORLD_MAP[8][8], pirate6),
#     Command(WORLD_MAP[8][8], WORLD_MAP[9][8], pirate6),
#     Command(WORLD_MAP[9][8], WORLD_MAP[10][8], pirate6),
#
#     Command(WORLD_MAP[10][8], WORLD_MAP[10][9], pirate6),  # перестроение снизу на следующий ряд справа
#
#     # ряд 9
#     Command(WORLD_MAP[10][9], WORLD_MAP[9][9], pirate6),  # полный ряд вверх
#     Command(WORLD_MAP[9][9], WORLD_MAP[8][9], pirate6),
#     Command(WORLD_MAP[8][9], WORLD_MAP[7][9], pirate6),
#     Command(WORLD_MAP[7][9], WORLD_MAP[6][9], pirate6),
#     Command(WORLD_MAP[6][9], WORLD_MAP[5][9], pirate6),
#     Command(WORLD_MAP[5][9], WORLD_MAP[4][9], pirate6),
#     Command(WORLD_MAP[4][9], WORLD_MAP[3][9], pirate6),
#     Command(WORLD_MAP[3][9], WORLD_MAP[2][9], pirate6),
#     Command(WORLD_MAP[2][9], WORLD_MAP[1][9], pirate6),
#
#     Command(WORLD_MAP[1][9], WORLD_MAP[1][10], pirate6),  # перестроение сверху на следующий ряд справа
#
#     # ряд 10
#     Command(WORLD_MAP[1][10], WORLD_MAP[2][10], pirate6),  # полный ряд вниз
#     Command(WORLD_MAP[2][10], WORLD_MAP[3][10], pirate6),
#     Command(WORLD_MAP[3][10], WORLD_MAP[4][10], pirate6),
#     Command(WORLD_MAP[4][10], WORLD_MAP[5][10], pirate6),
#     Command(WORLD_MAP[5][10], WORLD_MAP[6][10], pirate6),
#     Command(WORLD_MAP[6][10], WORLD_MAP[7][10], pirate6),
#     Command(WORLD_MAP[7][10], WORLD_MAP[8][10], pirate6),
#     Command(WORLD_MAP[8][10], WORLD_MAP[9][10], pirate6),
#     Command(WORLD_MAP[9][10], WORLD_MAP[10][10], pirate6),
#
#     Command(WORLD_MAP[10][10], WORLD_MAP[10][11], pirate6),  # перестроение снизу на следующий ряд справа
#
#     # ряд 11
#     Command(WORLD_MAP[10][11], WORLD_MAP[9][11], pirate6),  # полный ряд вверх
#     Command(WORLD_MAP[9][11], WORLD_MAP[8][11], pirate6),
#     Command(WORLD_MAP[8][11], WORLD_MAP[7][11], pirate6),
#     Command(WORLD_MAP[7][11], WORLD_MAP[6][11], pirate6),
#     Command(WORLD_MAP[6][11], WORLD_MAP[5][11], pirate6),
#     Command(WORLD_MAP[5][11], WORLD_MAP[4][11], pirate6),
#     Command(WORLD_MAP[4][11], WORLD_MAP[3][11], pirate6),
#     Command(WORLD_MAP[3][11], WORLD_MAP[2][11], pirate6),
#     Command(WORLD_MAP[2][11], WORLD_MAP[1][11], pirate6),  # меняю паттерн
#
#     # обход оставшегося внизу участка другим пиратом:
#     Command(WORLD_MAP[12][6], WORLD_MAP[11][6], pirate4),  # полный ряд вверх
#     Command(WORLD_MAP[11][6], WORLD_MAP[11][7], pirate4),
#     Command(WORLD_MAP[11][7], WORLD_MAP[11][8], pirate4),
#     Command(WORLD_MAP[11][8], WORLD_MAP[11][9], pirate4),
#     Command(WORLD_MAP[11][9], WORLD_MAP[11][10], pirate4),
# ]
