from constants import *


class Button:
    def __init__(self, image, x, y, size):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * size), int(height * size)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = 1

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = 0

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
