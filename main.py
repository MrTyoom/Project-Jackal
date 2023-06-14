import pygame.draw

from menu import MainMenu, PauseMenu
from constants import *
import ML
import audio
import cards
import constants


pause_button = Button(PAUSE_BUTTON_IMAGE, 0, 0, 0.65)
pause_button_clicked = Button(PAUSE_BUTTON_DARK_IMAGE, 0, 0, 0.65)
micro_button = Button(MICRO_BUTTON_IMAGE, 60, 0, 0.16)
micro_button_clicked = Button(MICRO_BUTTON_DARK_IMAGE, 60, 0, 0.16)
mute_button = Button(MUTE_BUTTON_IMAGE, 135, 0, 1.25)
unmute_button = Button(UNMUTE_BUTTON_IMAGE, 135, 0, 1.25)

# TESTS = queue.Queue()


def update_const():
    constants.MOVE += 1
    constants.TMP = 1


def update_pirates():
    if pirate1.move_possib > 1:
        pirate1.move_possib -= 1
    if pirate2.move_possib > 1:
        pirate2.move_possib -= 1
    if pirate3.move_possib > 1:
        pirate3.move_possib -= 1
    if pirate4.move_possib > 1:
        pirate4.move_possib -= 1
    if pirate5.move_possib > 1:
        pirate5.move_possib -= 1
    if pirate6.move_possib > 1:
        pirate6.move_possib -= 1


class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.playing, self.running = True, True
        self.START_KEY, self.BACK_KEY, self.KEY_DOWN, self.KEY_UP = False, False, False, False
        self.RIGHT_KEY, self.LEFT_KEY = False, False
        self.coin_counter1, self.coin_counter2 = 0, 0
        self.cur_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        # self.options_menu = OptionsMenu(self)
        self.clock = pygame.time.Clock()
        self.flag = 2   # just for initialisation ship tiles by pirates
        self.counter, self.bttn = -1, 1
        pygame.display.set_caption("JACKAL")

    # function for checking an event
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False, False
                self.cur_menu.display_run, self.pause_menu.display_run = False, False
            if event.type == pygame.KEYDOWN:
                if self.cur_menu.display_run:
                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True
                    if event.key == pygame.K_UP:
                        self.KEY_UP = True
                    if event.key == pygame.K_DOWN:
                        self.KEY_DOWN = True
                elif self.pause_menu.display_run:
                    if event.key == pygame.K_RETURN:
                        self.START_KEY = True
                    if event.key == pygame.K_UP:
                        self.KEY_UP = True
                    if event.key == pygame.K_DOWN:
                        self.KEY_DOWN = True
                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True
                    if event.key == pygame.K_RETURN:
                        self.counter += 1
                        constants.MOVE += 1
                        constants.TMP = 1

                else:
                    if event.key == pygame.K_BACKSPACE:
                        self.BACK_KEY = True
                    if event.key == pygame.K_RIGHT:
                        self.RIGHT_KEY = True
                    if event.key == pygame.K_LEFT:
                        self.LEFT_KEY = True
                    if event.key == pygame.K_RETURN:
                        self.counter += 1
                        constants.MOVE += 1
                        update_pirates()

    # function which reset values of keys for their original condition
    def update_keys(self):
        self.KEY_UP, self.KEY_DOWN, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    # function for placing text on the screen, with fixed size and font
    def text(self, text, size, x, y, font_name):
        font = pygame.font.Font(font_name, size)
        text_display = font.render(text, True, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_display, text_rect)

    # function which rewrites all the sprites in the game field
    def blit_pirates(self):
        if GLOBAL_PIRATES[0].live:
            self.display.blit(pygame.transform.scale(PIRATE_1, (W1 * 0.75, H1 * 0.75)), (WIDTH - 400, 110))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_1, (W1 * 0.75, H1 * 0.75)), (WIDTH - 400, 110))

        if GLOBAL_PIRATES[1].live:
            self.display.blit(pygame.transform.scale(PIRATE_2, (W2 * 0.9, H2 * 0.9)), (WIDTH - 250, 100))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_2, (W2 * 0.9, H2 * 0.9)), (WIDTH - 250, 100))

        if GLOBAL_PIRATES[2].live:
            self.display.blit(pygame.transform.scale(PIRATE_3, (W3, H3)), (WIDTH - 135, 115))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_3, (W3, H3)), (WIDTH - 135, 115))

        if GLOBAL_PIRATES[3].live:
            self.display.blit(pygame.transform.scale(PIRATE_4, (W4 * 0.72, H4 * 0.72)), (WIDTH - 400, 450))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_4, (W4 * 0.72, H4 * 0.72)), (WIDTH - 400, 450))

        if GLOBAL_PIRATES[4].live:
            self.display.blit(pygame.transform.scale(PIRATE_5, (W5 * 0.65, H5 * 0.65)), (WIDTH - 260, 460))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_5, (W5 * 0.65, H5 * 0.65)), (WIDTH - 260, 460))

        if GLOBAL_PIRATES[5].live:
            self.display.blit(pygame.transform.scale(PIRATE_6, (W6 * 0.8, H6 * 0.8)), (WIDTH - 130, 450))
        else:
            self.display.blit(pygame.transform.scale(DEAD_PIRATE_6, (W6 * 0.8, H6 * 0.8)), (WIDTH - 130, 450))

        self.display.blit(pygame.transform.scale(COIN, (60, 61)), (WIDTH - 170, 40))
        self.display.blit(pygame.transform.scale(COIN, (60, 61)), (WIDTH - 170, 645))

        self.text(f'x{self.coin_counter1}', 80, WIDTH - 60, 74, MY_FONT)
        self.text(f'x{self.coin_counter2}', 80, WIDTH - 60, 684, MY_FONT)

        if constants.MOVE % 2 == 1:
            self.text("Player 1", 70, 100, 400, MY_FONT)
        else:
            self.text("Player 2", 70, 100, 400, MY_FONT)

    def blit_all_chips(self, prt: Pirate, x: float, y: float):
        if prt.number == 0:
            pygame.draw.circle(self.display, (255, 215, 0), (y * FIELD_SIZE_Y + 7.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('1', 13, y * FIELD_SIZE_Y + 7.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))
        elif prt.number == 1:
            pygame.draw.circle(self.display, (255, 215, 0), (y * FIELD_SIZE_Y + 27.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('2', 13, y * FIELD_SIZE_Y + 27.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))
        elif prt.number == 2:
            pygame.draw.circle(self.display, (255, 215, 0), (y * FIELD_SIZE_Y + 47.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('3', 13, y * FIELD_SIZE_Y + 47.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))
        elif prt.number == 3:
            pygame.draw.circle(self.display, (250, 128, 128), (y * FIELD_SIZE_Y + 7.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('1', 13, y * FIELD_SIZE_Y + 7.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))
        elif prt.number == 4:
            pygame.draw.circle(self.display, (250, 128, 128), (y * FIELD_SIZE_Y + 27.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('2', 13, y * FIELD_SIZE_Y + 27.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))
        elif prt.number == 5:
            pygame.draw.circle(self.display, (250, 128, 128), (y * FIELD_SIZE_Y + 47.5, x * FIELD_SIZE_X + 27.5), 7.5)
            self.text('3', 13, y * FIELD_SIZE_Y + 47.5, x * FIELD_SIZE_X + 26.5, pygame.font.match_font('arial'))

    # function, have to process command, but it doesn't work properly
    # due to incorrect data
    # works correct with ships and right-left pirate moving
    def processing_command(self, cmd: tuple, s: str):
        if len(cmd) == 2:
            if cmd[0] == 101 and constants.MOVE % 2:
                self.movement_ship(s, 1)
            elif cmd[0] == 101 and not constants.MOVE % 2:
                self.movement_ship(s, 2)
            else:
                if constants.MOVE % 2 and GLOBAL_PIRATES[cmd[0]].live and GLOBAL_PIRATES[cmd[0]].move_possib == 1:
                    for y in range(len(WORLD_MAP)):
                        for x in range(len(WORLD_MAP[y])):
                            if GLOBAL_PIRATES[cmd[0]] in WORLD_MAP[y][x].pirates:
                                try:
                                    if cmd[1] == 0:
                                        TESTS.put(Command(WORLD_MAP[y][x], WORLD_MAP[y][x - 1], GLOBAL_PIRATES[cmd[0]]))
                                    elif cmd[1] == 1:
                                        TESTS.put(Command(WORLD_MAP[y][x], WORLD_MAP[y][x + 1], GLOBAL_PIRATES[cmd[0]]))
                                    elif cmd[1] == 2:
                                        TESTS.put(Command(WORLD_MAP[y][x], WORLD_MAP[y - 1][x], GLOBAL_PIRATES[cmd[0]]))
                                    else:
                                        TESTS.put(Command(WORLD_MAP[y][x], WORLD_MAP[y + 1][x], GLOBAL_PIRATES[cmd[0]]))
                                except IndexError:
                                    print("Illegal move, try again")


    def movement_ship(self, command, num):
        intent = CODES_TO_INTENTS[audio.predict_intent_code(command)]

        i = [len(WORLD_MAP) - 1 if num == 1 else 0][0]
        if intent == CODES_TO_INTENTS[1]:
            for j in range(len(WORLD_MAP)):
                if WORLD_MAP[i][j].code == num + 100:
                    if j + 1 < len(WORLD_MAP) - 1:
                        WORLD_MAP[i][j + 1], WORLD_MAP[i][j] = WORLD_MAP[i][j], WORLD_MAP[i][j + 1]
                        if num == 1:
                            SHIP1_COORD['y'] = j + 1
                        else:
                            SHIP2_COORD['y'] = j + 1
                        break

        elif intent == CODES_TO_INTENTS[0]:
            for j in range(len(WORLD_MAP)):
                if WORLD_MAP[i][j].code == num + 100:
                    if j - 1 >= 1:
                        WORLD_MAP[i][j - 1], WORLD_MAP[i][j] = WORLD_MAP[i][j], WORLD_MAP[i][j - 1]
                        if num == 1:
                            SHIP1_COORD['y'] = j - 1
                        else:
                            SHIP2_COORD['y'] = j - 1
                        break

    def card_events(self, was: Tile, go: Tile, pirate: Pirate):
        if go.code == 1:
            if constants.TMP == 1:
                self.card_events(go, cards.arrow(was, go, pirate, go.code), pirate)
                constants.TMP -= 1
        elif go.code == 2:
            cards.arrow(was, go, pirate, go.code)
            self.card_events(go, WORLD_MAP[go.y][go.x + 1], pirate)
        elif go.code == 3:
            if constants.TMP == 1:
                self.card_events(go, cards.arrow(was, go, pirate, go.code), pirate)
                constants.TMP -= 1
            self.card_events(go, WORLD_MAP[go.y - 1][go.x + 1], pirate)
        elif go.code == 4:
            cards.arrow(was, go, pirate, go.code)
            self.card_events(go, WORLD_MAP[go.y][go.x + 1], pirate)
        elif go.code == 5:
            cards.arrow(was, go, pirate, go.code)
            self.card_events(go, WORLD_MAP[go.y][go.x + 1], pirate)
        elif go.code == 6:
            cards.arrow(was, go, pirate, go.code)
            self.card_events(go, WORLD_MAP[go.y][go.x + 1], pirate)
        elif go.code == 7:
            cards.arrow(was, go, pirate, go.code)
            self.card_events(go, WORLD_MAP[go.y][go.x + 1], pirate)
        elif go.code == 8:
            cards.balloon(was, go, pirate)
        elif go.code == 9:
            cards.barrel(was, go, pirate)
        elif go.code == 10:
            cards.cannibal(was, go, pirate)
        elif go.code == 11:
            cards.castle(was, go, pirate)
        elif go.code == 12:
            cards.castle_girl(was, go, pirate)
        elif go.code == 13:
            cards.croc(was, go, pirate)
            self.card_events(go, was, pirate)
        elif 14 <= go.code <= 18:
            cards.gold(was, go, pirate)
            if pirate.team == 1 and constants.TMP == 1:
                self.coin_counter2 += go.code - 13
                constants.TMP -= 1
            elif pirate.team == 2 and constants.TMP == 1:
                self.coin_counter1 += go.code - 13
                constants.TMP -= 1
        elif go.code == 19:
            cards.horse(was, go, pirate)
        elif go.code == 20:
            cards.ice(was, go, pirate)
        elif 21 <= go.code <= 24:
            cards.labyrinth(was, go, pirate, go.code - 19)
        elif 25 <= go.code <= 28:
            cards.nothing(was, go, pirate)
        elif go.code == 29:
            if constants.TMP == 1:
                self.card_events(go, cards.plane(was, go, pirate), pirate)
                constants.TMP -= 1
        elif go.code == 30:
            cards.trap(was, go, pirate)
        elif go.code == 31:
            cards.cannon(was, go, pirate)
        # elif go.code == 100:
        #     go.pirates[pirate.number] = 1
        #     was.pirates[pirate.number] = 0
        #     if pirate.team == 1:
        #         if pirate.gold:
        #             self.coin_counter1 += 1
        #     else:
        #         pirate.live = 0
        #         GLOBAL_PIRATES[pirate.number], go.pirates[pirate.number] = 0, 0
        # elif go.code == 101:
        #     go.pirates[pirate.number] = 1
        #     was.pirates[pirate.number] = 0
        #     if pirate.team == 2:
        #         if pirate.gold:
        #             self.coin_counter2 += 1
        #     else:
        #         pirate.live = 0
        #         GLOBAL_PIRATES[pirate.number], go.pirates[pirate.number] = 0, 0

    def draw_field(self):
        start_coord_y = 0.7
        for row in WORLD_MAP:
            start_coord_x = 3

            for tile in row:
                if tile.code == 101:
                    if self.flag > 0:
                        self.flag -= 1
                        tile.pirates[0:3] = [pirate1, pirate2, pirate3]
                        self.display.blit(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                    else:
                        self.display.blit(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                elif tile.code == 102:
                    if self.flag > 0:
                        self.flag -= 1
                        tile.pirates[3:] = [pirate4, pirate5, pirate6]
                        self.display.blit(
                            pygame.transform.rotate(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)), 180),
                            (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                    else:
                        self.display.blit(
                            pygame.transform.rotate(pygame.transform.scale(SHIP_IMAGE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                                    180),
                            (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                elif tile.code != 0:
                    if not tile.closed:
                        self.display.blit(pygame.transform.scale(CODE_TO_TILE[tile.code], (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                    else:
                        self.display.blit(pygame.transform.scale(CLOSED_FIELD_TILE, (FIELD_SIZE_X, FIELD_SIZE_Y)),
                                          (FIELD_SIZE_X * start_coord_x, FIELD_SIZE_Y * start_coord_y))
                for prt in tile.pirates:
                    if isinstance(prt, Pirate):
                        self.blit_all_chips(prt, start_coord_y, start_coord_x)
                start_coord_x += 1
            start_coord_y += 1

    def game_loop(self):
        while self.playing:
            self.events()
            if self.BACK_KEY:
                self.playing = False

            self.display.fill((140, 220, 224))

            micro_button.draw(self.display)

            if pause_button.draw(self.display):
                if pause_button.clicked or self.pause_menu.display_run:
                    game.pause_menu.display_menu()

            if self.bttn % 2:
                if unmute_button.draw(self.display):
                    if unmute_button.clicked:
                        pygame.mixer_music.set_volume(0)
                        self.bttn += 1
            else:
                if mute_button.draw(self.display):
                    if mute_button.clicked:
                        pygame.mixer_music.set_volume(0.1)
                        self.bttn += 1

            update_pirates()
            self.blit_pirates()
            self.draw_field()

            try:
                if micro_button.clicked:
                    s = audio.speech_to_text(5)
                    print(s)
                    self.processing_command(ML.input_for_gui(s), s)
                    update_pirates()
                    update_const()
            except:
                print('Repeat your phrase')

            self.WINDOW.blit(self.display, (0, 0))

            pygame.display.update()
            self.update_keys()
            self.clock.tick(FPS)

            # while not TESTS.empty():
            #     a = TESTS.get()
            #     self.card_events(a.was, a.go, a.pirate)

            if self.counter != -1:
                self.card_events(TESTS[self.counter].was, TESTS[self.counter].go, TESTS[self.counter].pirate)



if __name__ == "__main__":
    game = Game()

    pygame.mixer_music.load('video_audio/main_theme (online-audio-converter.com).mp3')
    pygame.mixer_music.set_volume(0.1)
    pygame.mixer_music.play(-1)

    while game.running:
        game.cur_menu.display_menu()
        game.game_loop()
