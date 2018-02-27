import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets\\bird_sing.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = y

    def update(self):
        self.rect.y = self.height

    def reset_position(self):
        self.rect.y = self.height
