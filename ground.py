import pygame
import config as cfg

class Ground(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load('assets\\ground.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * cfg.GROUND_WIDTH
        self.rect.y = 320

    def update(self):
        if self.rect.x <= -1 * cfg.GROUND_WIDTH + 1:
            self.reset_position()
        else:
            self.rect.x -= cfg.GAME_SPEED

    def reset_position(self):
        self.rect.x = (cfg.numGround - 1) * cfg.GROUND_WIDTH
