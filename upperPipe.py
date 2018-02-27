import pygame

class UpperPipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets\\tube1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if (self.rect.x == -52):
            self.reset_pos()
        else:
            self.rect.x -= 1

    def reset_pos(self):
        self.rect.x = 400
