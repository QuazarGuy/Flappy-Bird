import pygame
import config as cfg

class Ground(pygame.sprite.Sprite):
    # Initializes a ground piece, takes a number representing its position index
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load('assets\\ground.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * cfg.GROUND_WIDTH
        self.rect.y = 320

    # Updates the position of the ground, calls reset_pos if off screen
    def update(self):
        if self.rect.x <= -1 * cfg.GROUND_WIDTH + 1:
            self.reset_pos()
        else:
            self.rect.x -= cfg.GAME_SPEED

    # Resets the position of the ground to the right side of the screen
    def reset_pos(self):
        self.rect.x = (cfg.numGround - 1) * cfg.GROUND_WIDTH
