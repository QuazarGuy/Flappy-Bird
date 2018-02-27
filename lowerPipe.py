import pygame
import config as cfg

class LowerPipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets\\tube2.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * cfg.PIPE_DISTANCE + cfg.numPipes * cfg.PIPE_DISTANCE
        self.rect.y = y + cfg.PIPE_GAP

    def update(self):
        if self.rect.x <= -1 * cfg.PIPE_DISTANCE + 1:
            self.reset_pos()
        else:
            self.rect.x -= cfg.GAME_SPEED

    def reset_pos(self):
        self.rect.x = (cfg.numPipes - 1) * cfg.PIPE_DISTANCE
