import pygame

PAUSE_BUTTON_IMAGE = pygame.image.load('images/dark_pause_button.png')
MICRO_BUTTON_IMAGE = pygame.image.load('images/micro_button.png')
MICRO_BUTTON_DARK_IMAGE = pygame.image.load('images/micro_button_dark.png')
PAUSE_BUTTON_DARK_IMAGE = pygame.image.load('images/pause_button_dark.png')
MUTE_BUTTON_IMAGE = pygame.image.load('images/mute_button.png')
MUTE_BUTTON_DARK_IMAGE = pygame.image.load('images/mute_button_dark.png')
UNMUTE_BUTTON_IMAGE = pygame.image.load('images/unmute_button.png')
UNMUTE_BUTTON_DARK_IMAGE = pygame.image.load('images/unmute_button_dark.png')

CLICKED_BUTTON = {
    MICRO_BUTTON_IMAGE: MICRO_BUTTON_DARK_IMAGE,
    PAUSE_BUTTON_IMAGE: PAUSE_BUTTON_DARK_IMAGE,
    UNMUTE_BUTTON_IMAGE: UNMUTE_BUTTON_DARK_IMAGE,
    MUTE_BUTTON_IMAGE: MUTE_BUTTON_DARK_IMAGE
}


class Button:
    def __init__(self, image, x, y, size):
        self.width, self.height = image.get_width(), image.get_height()
        self.size = size
        self.original_image = image
        self.image = pygame.transform.scale(image, (int(self.width * size), int(self.height * size)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(CLICKED_BUTTON[self.original_image], (int(self.width * self.size),
                                                                                    int(self.height * self.size)))
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = 1

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(self.original_image, (int(self.width * self.size), int(self.height * self.size)))
            self.clicked = 0

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Tile:
    __slots__ = ("x", "y", "pirates", "closed", "code", "gold")

    def __init__(self, code):
        self.x = None
        self.y = None
        self.pirates = [0, 0, 0, 0, 0, 0]
        self.closed = 1
        self.code = code
        self.gold = 0


class Pirate:
    __slots__ = ("team", "number", "move_possib", "live", "gold")

    def __init__(self, team, number):
        self.team = team
        self.number = number
        self.move_possib = 1
        self.live = 1
        self.gold = 0
