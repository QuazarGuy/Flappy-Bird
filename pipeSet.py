import pygame
import config as cfg
from random import randint
from upperPipe import UpperPipe
from lowerPipe import LowerPipe

class PipeSet(pygame.sprite.Sprite):
    # Initializes a set of upper and lower pipes at a random height given an index
    # in the number of pipe sets and a sprite group list to add the pipes to, so
    # collide can be called on them.
    def __init__(self, x, enemy_list):
        super().__init__()
        y = randint(0, 15) * 10 + cfg.PIPE_HEIGHT
        self.upperPipe = UpperPipe(x, y)
        self.lowerPipe = LowerPipe(x, y + cfg.PIPE_GAP)
        enemy_list.add(self.upperPipe)
        enemy_list.add(self.lowerPipe)

    # Updates the position of the upper and lower pipes in the set and resets their
    # position if they are off the screen with a new random height
    def update(self):
        if self.upperPipe.rect.x <= -1 * cfg.PIPE_DISTANCE + 1:
            x = (cfg.numPipes - 1) * cfg.PIPE_DISTANCE
            self.upperPipe.rect.x = x
            self.lowerPipe.rect.x = x
            y = randint(0, 15) * 10 + cfg.PIPE_HEIGHT
            self.upperPipe.rect.y = y
            self.lowerPipe.rect.y = y + cfg.PIPE_GAP
        else:
            self.upperPipe.rect.x -= 1
            self.lowerPipe.rect.x -= 1
