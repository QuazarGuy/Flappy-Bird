import pygame
import config as cfg

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets\\bird_sing.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = cfg.OFFSET
        self.rect.y = cfg.START_HEIGHT
        self.y_velocity = 0

    # Updates the bird's position, flies if mouse clicked or spacebar pressed
    def update(self, event):
        click = pygame.mouse.get_pressed()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or click[0] == 1:
            self.y_velocity = cfg.MAX_RISE
        elif self.y_velocity < cfg.MAX_FALL:
            self.y_velocity += 1
        else:
            self.y_velocity = cfg.MAX_FALL
        self.rect.y = self.rect.y + self.y_velocity

    # Checks if the bird has collided with the ground, pipes, or top edge of the screen and quits if True
    def checkCollision(self, enemy_list):
        if pygame.sprite.spritecollideany(self, enemy_list, collided = None) or self.rect.y < -2:
            quit()
