import pygame.sprite

from constants import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.middle_w, self.middle_h = WIDTH / 2, HEIGHT / 2
        self.display_run = True
        self.cursor_rect = pygame.rect.Rect(0, 0, 20, 20)
        self.temp = -60

    def draw_cursor(self):
        self.game.text('>', 30, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.WINDOW.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.update_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.start_x, self.start_y = self.middle_w + 110, self.middle_h + 60
        self.options_x, self.options_y = self.middle_w + 110, self.middle_h + 100
        self.quit_x, self.quit_y = self.middle_w + 110, self.middle_h + 140
        self.cursor_rect.midtop = (self.start_x + self.temp, self.start_y)

    def display_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.events()
            self.check_input()
            self.game.display.blit(MENU_BACKGROUND, (0, 0))
            self.game.text("Jackal", 50, self.middle_w, 30)
            self.game.text("Start", 30, self.start_x, self.start_y)
            self.game.text("Options", 30, self.options_x, self.options_y)
            self.game.text("Quit", 30, self.quit_x, self.quit_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.KEY_DOWN:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.options_x + self.temp, self.options_y)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.quit_x + self.temp, self.quit_y)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.start_x + self.temp, self.start_y)
                self.state = "Start"
        elif self.game.KEY_UP:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.quit_x + self.temp, self.quit_y)
                self.state = "Quit"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.start_x + self.temp, self.start_y)
                self.state = "Start"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.options_x + self.temp, self.options_y)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                pass
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False

            self.display_run = False



