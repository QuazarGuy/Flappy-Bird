import pygame
import config as cfg

class Score():
    # Initializes the score to 0
    def __init__(self):
        self.count = 0
        self.timer = cfg.numPipes * cfg.PIPE_DISTANCE

    # Updates the score if the player passes a pipe
    def update(self):
        if self.timer <= 0:
            self.count += 1
            self.timer = cfg.PIPE_DISTANCE
        else:
            self.timer -= cfg.GAME_SPEED

    # Renders the score on the given screen
    def draw(self, screen):
        font = pygame.font.SysFont(None, 28, False)
        text = font.render("Score: " + str(self.count), True, (255, 255, 255))
        screen.blit(text, (5, 5))
