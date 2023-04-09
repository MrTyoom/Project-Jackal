import pygame

import audio
from buttons import Button
from menu import MainMenu
from constants import *

# start_button = Button(START_BUTTON_IMAGE, 370, 200, 0.5)
# quit_button = Button(QUIT_BUTTON_IMAGE, 370, 400, 0.5)
# options_button = Button(OPTIONS_BUTTON_IMAGE, 370, 300, 0.5)
pause_button = Button(PAUSE_BUTTON_IMAGE, 0, 0, 0.5)
pause_button_clicked = Button(PAUSE_BUTTON_DARK_IMAGE, 0, 0, 0.5)
micro_button = Button(MICRO_BUTTON_IMAGE, 50, 0, 0.12)
micro_button_clicked = Button(MICRO_BUTTON_DARK_IMAGE, 50, 0, 0.12)


class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.playing, self.running = True, True
        self.font_name = pygame.font.match_font('arial')
        self.START_KEY, self.BACK_KEY, self.KEY_DOWN, self.KEY_UP = False, False, False, False
        self.RIGHT_KEY, self.LEFT_KEY = False, False
        self.rom_counter1, self.rom_counter2 = 0, 0
        self.coin_counter1, self.coin_counter2 = 0, 0
        self.cur_menu = MainMenu(self)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("JACKAL")

    # function for checking an event
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False
                self.cur_menu.display_run = False
            if event.type == pygame.KEYDOWN:
                if self.cur_menu.display_run:
                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True
                    if event.key == pygame.K_UP:
                        self.KEY_UP = True
                    if event.key == pygame.K_DOWN:
                        self.KEY_DOWN = True
                else:
                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True
                    if event.key == pygame.K_RIGHT:
                        self.RIGHT_KEY = True
                    if event.key == pygame.K_LEFT:
                        self.LEFT_KEY = True

    # function which reset values of keys for their original condition
    def update_keys(self):
        self.KEY_UP, self.KEY_DOWN, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    # function for placing text on the screen, with fixed size and font
    def text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_display = font.render(text, True, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_display, text_rect)

    # function which rewrites all the sprites in the game field
    def blit_pirates(self):
        self.display.blit(pygame.transform.scale(PIRATE_1, (75, 109)), (WIDTH - 300, 110))
        self.display.blit(pygame.transform.scale(PIRATE_2, (65, 121)), (WIDTH - 200, 100))
        self.display.blit(pygame.transform.scale(PIRATE_3, (82, 105)), (WIDTH - 100, 118))
        self.display.blit(pygame.transform.scale(PIRATE_4, (80, 117)), (WIDTH - 300, 500))
        self.display.blit(pygame.transform.scale(PIRATE_5, (75, 110)), (WIDTH - 200, 510))
        self.display.blit(pygame.transform.scale(PIRATE_6, (80, 120)), (WIDTH - 100, 500))
        self.display.blit(pygame.transform.scale(ROM, (74, 90)), (WIDTH - 300, 10))
        self.display.blit(pygame.transform.scale(ROM, (74, 90)), (WIDTH - 300, 620))
        self.display.blit(pygame.transform.scale(COIN, (60, 61)), (WIDTH - 150, 30))
        self.display.blit(pygame.transform.scale(COIN, (60, 61)), (WIDTH - 150, 640))

        self.text(f'x{self.rom_counter1}', 40, WIDTH - 210, 74)
        self.text(f'x{self.rom_counter2}', 40, WIDTH - 210, 684)
        self.text(f'x{self.coin_counter1}', 40, WIDTH - 60, 74)
        self.text(f'x{self.coin_counter2}', 40, WIDTH - 60, 684)

    def movement_ship(self, command):
        intent = CODES_TO_INTENTS[audio.predict_intent_code(command)]

        i = len(WORLD_MAP) - 1
        if intent == CODES_TO_INTENTS[1]:
            for j in range(len(WORLD_MAP)):
                if WORLD_MAP[i][j] == "S1":
                    if j + 1 < len(WORLD_MAP) - 1:
                        WORLD_MAP[i][j + 1], WORLD_MAP[i][j] = WORLD_MAP[i][j], WORLD_MAP[i][j + 1]
                        break

        elif intent == CODES_TO_INTENTS[0]:
            for j in range(len(WORLD_MAP)):
                if WORLD_MAP[i][j] == "S1":
                    if j - 1 >= 1:
                        WORLD_MAP[i][j - 1], WORLD_MAP[i][j] = WORLD_MAP[i][j], WORLD_MAP[i][j - 1]
                        break

    def draw_field(self):
        start_coord_y = 1
        for row in WORLD_MAP:
            start_coord_x = 1
            for tile in row:
                if tile == 'S1':
                    self.display.blit(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                      (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                elif tile == "S2":
                    self.display.blit(
                        pygame.transform.rotate(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)), 180),
                        (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                elif tile == 'x':
                    self.display.blit(pygame.transform.scale(CLOSED_FIELD_TILE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                      (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                start_coord_x += 1
            start_coord_y += 1

    def game_loop(self):
        while self.playing:
            self.events()
            if self.BACK_KEY:
                self.playing = False

            self.display.fill((140, 220, 224))

            # piece of code, which checks correctness of rom and coin counters
            if pause_button.draw(self.display):
                self.coin_counter1 += pause_button.clicked
                self.rom_counter1 += pause_button.clicked
            if micro_button.draw(self.display):
                self.coin_counter2 += micro_button.clicked
                self.rom_counter2 += micro_button.clicked

            self.blit_pirates()
            self.draw_field()

            if micro_button.clicked:
                s = audio.speech_to_text(3)
                self.movement_ship(s)

            self.WINDOW.blit(self.display, (0, 0))

            pygame.display.update()
            self.update_keys()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()

    while game.running:
        game.cur_menu.display_menu()
        game.game_loop()
