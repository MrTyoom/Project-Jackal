from constants import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.middle_w, self.middle_h = WIDTH / 2, HEIGHT / 2
        self.display_run = True
        self.cursor_rect = pygame.rect.Rect(0, 0, 20, 20)
        self.temp = -60

    def draw_cursor(self):
        self.game.text('>', 60, self.cursor_rect.x - 50, self.cursor_rect.y, MY_FONT)

    def blit_screen(self):
        self.game.WINDOW.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.update_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.start_x, self.start_y = self.middle_w + 200, self.middle_h + 55
        self.options_x, self.options_y = self.middle_w + 170, self.middle_h + 115
        self.quit_x, self.quit_y = self.middle_w + 200, self.middle_h + 185
        self.cursor_rect.midtop = (self.start_x + self.temp, self.start_y)
        self.screen = self.game.WINDOW.blit(self.game.display, (0, 0))

    def display_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.events()
            self.check_input()
            self.game.display.blit(MENU_BACKGROUND, (0, 0))
            self.game.text("Jackal", 100, self.middle_w, 40, MY_FONT)
            self.game.text("Start", 90, self.start_x, self.start_y, MY_FONT)
            self.game.text("Options", 90, self.options_x, self.options_y, MY_FONT)
            self.game.text("Quit", 90, self.quit_x, self.quit_y, MY_FONT)
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
                self.game.playing = False
                print("See soon")
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False

            self.display_run = False


# to be honest, MainMenu and PauseMenu are same, except some things: resume, and no title
class PauseMenu(MainMenu):
    def __init__(self, game):
        MainMenu.__init__(self, game)
        # self.display_run = False
        self.state = "Resume"
        self.resume_x, self.resume_y = self.middle_w + 170, self.middle_h + 60
        self.cursor_rect.midtop = (self.resume_x + self.temp, self.resume_y)

    def display_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.events()
            self.check_input()
            self.game.display.blit(MENU_BACKGROUND, (0, 0))
            # self.game.text("Jackal", 50, self.middle_w, 30)
            self.game.text("Resume", 90, self.resume_x + 10, self.resume_y, MY_FONT)
            self.game.text("Options", 90, self.options_x, self.options_y + 10, MY_FONT)
            self.game.text("Quit", 90, self.quit_x, self.quit_y + 15, MY_FONT)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.KEY_DOWN:
            if self.state == "Resume":
                self.cursor_rect.midtop = (self.options_x + self.temp - 5, self.options_y + 12)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.quit_x + self.temp + 20, self.quit_y + 5)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.resume_x + self.temp, self.resume_y)
                self.state = "Resume"
        elif self.game.KEY_UP:
            if self.state == "Resume":
                self.cursor_rect.midtop = (self.quit_x + self.temp + 20, self.quit_y + 5)
                self.state = "Quit"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.resume_x + self.temp, self.resume_y)
                self.state = "Resume"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.options_x + self.temp - 5, self.options_y + 12)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Resume":
                self.game.playing = True
            elif self.state == "Options":
                self.game.playing = False
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False

            self.display_run = False
