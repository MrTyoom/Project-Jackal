from constants import *


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
