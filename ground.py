import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, display_width):
        super().__init__()
        self.image = pygame.image.load('assets\\ground.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 320
        self.display_width = display_width

    def update(self):
        if self.rect.x == -336:
            self.reset_position()
        else:
            self.rect.x -= 1

    def reset_position(self):
        self.rect.x = (self.display_width / 336 + 1) * 336
