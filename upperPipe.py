import pygame
import config as cfg

class UpperPipe(pygame.sprite.Sprite):
    # Initializes a ground piece, takes a number representing its position index and height
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets\\tube1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * cfg.PIPE_DISTANCE + cfg.numPipes * cfg.PIPE_DISTANCE
        self.rect.y = y

    # Updates the position of the pipe, calls reset_pos if off screen
    def update(self):
        if self.rect.x <= -1 * cfg.PIPE_DISTANCE + 1:
            self.reset_pos()
        else:
            self.rect.x -= cfg.GAME_SPEED

    # Resets the position of the pipe to the right side of the screen
    def reset_pos(self):
        self.rect.x = (cfg.numPipes - 1) * cfg.PIPE_DISTANCE
