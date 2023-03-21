import pygame.transform

import audio
from buttons import Button
from menu import MainMenu
from constants import *

# start_button = Button(START_BUTTON_IMAGE, 370, 200, 0.5)
# quit_button = Button(QUIT_BUTTON_IMAGE, 370, 400, 0.5)
# options_button = Button(OPTIONS_BUTTON_IMAGE, 370, 300, 0.5)
pause_button = Button(PAUSE_BUTTON_IMAGE, 0, 0, 0.5)
micro_button = Button(MICRO_BUTTON_IMAGE, 50, 0, 0.12)


class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.playing, self.running = True, True
        self.font_name = pygame.font.match_font('arial')
        self.START_KEY, self.BACK_KEY, self.KEY_DOWN, self.KEY_UP = False, False, False, False
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
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP:
                    self.KEY_UP = True
                if event.key == pygame.K_DOWN:
                    self.KEY_DOWN = True

    # function which reset values of keys for their original condition
    def update_keys(self):
        self.KEY_UP, self.KEY_DOWN, self.START_KEY, self.BACK_KEY = False, False, False, False

    # function for placing text on the screen, with fixed size and font
    def text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_display = font.render(text, True, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_display, text_rect)

    def game_loop(self):
        while self.playing:
            self.events()
            if self.START_KEY:
                self.playing = False

            self.display.fill((140, 220, 224))

            start_coord_y = 1
            for row in WORLD_MAP:
                start_coord_x = 1
                for tile in row:
                    if tile == 'S':
                        self.display.blit(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                    elif tile == 'x':
                        self.display.blit(pygame.transform.scale(CLOSED_FIELD_TILE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                    start_coord_x += 1
                start_coord_y += 1

            pause_button.draw(self.display)
            micro_button.draw(self.display)

            if micro_button.clicked:
                s = audio.speech_to_text(5)
                print(s)
                if 'выход' in s.lower():
                    self.running, self.playing = False, False

            # write logic for calling menu
            # if pause_button.clicked:
            #     print('Game paused')
            #     pass

            self.WINDOW.blit(self.display, (0, 0))

            pygame.display.update()
            self.update_keys()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()

    while game.running:
        game.cur_menu.display_menu()
        game.game_loop()
