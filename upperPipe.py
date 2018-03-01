import pygame
import config as cfg
from lowerPipe import LowerPipe

class UpperPipe(pygame.sprite.Sprite):
    # Initializes a ground piece, takes a number representing its position index and height
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets\\tube1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * cfg.PIPE_DISTANCE + cfg.numPipes * cfg.PIPE_DISTANCE
        self.rect.y = y
