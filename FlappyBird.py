# Name        : FlappyBird.py
# Authors     : Robin Shaw, Jeff Talada
# Date        : 2/27/18
# Description : Allows a user to play Flappy Bird. See config.py to adjust settings.

import pygame
import config as cfg
from ground import Ground
from pipeSet import PipeSet
from upperPipe import UpperPipe
from lowerPipe import LowerPipe
from bird import Bird
from score import Score

pygame.init()

gameDisplay = pygame.display.set_mode((cfg.DISPLAY_WIDTH, cfg.DISPLAY_HEIGHT))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
score = Score()
started = False
playing = True

background = pygame.image.load('assets\\bg.png')

# Initializes the ground and pipes and add them to the enemy_list
def initEnemies():
    x = 0
    while (x < cfg.numPipes):
        pipeSet = PipeSet(x, enemy_list)
        pipeSets.append(pipeSet)
        x += 1
    x = 0
    while (x < cfg.numGround):
        ground = Ground(x)
        enemy_list.add(ground)
        x += 1

# Draws the background
def drawBackground():
    x = 0
    while (x < cfg.numBackgrounds):
        gameDisplay.blit(background, (x * cfg.BACKGROUND_WIDTH, -10))
        x += 1

# Draws the start button
def drawStartButton():
    pygame.draw.rect(gameDisplay, (255, 255, 255),
                     (cfg.DISPLAY_WIDTH / 2 - 80,
                     cfg.DISPLAY_HEIGHT / 2 - 25,
                     160, 50))
    font = pygame.font.SysFont(None, 50, False)
    text = font.render("Start!", True, (0, 0, 0))
    gameDisplay.blit(text, (cfg.DISPLAY_WIDTH / 2 - 45, cfg.DISPLAY_HEIGHT / 2 - 15))


bird = Bird()
player_list = pygame.sprite.Group() # Player sprite
player_list.add(bird)
pipeSets = []
enemy_list = pygame.sprite.Group()  # Enemy sprites
initEnemies()

# Start screen
while not started:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Check if button clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (cfg.DISPLAY_WIDTH / 2 - 80 < mouse[0] < cfg.DISPLAY_WIDTH / 2 + 80
         and cfg.DISPLAY_HEIGHT / 2 - 50 < mouse[1] < cfg.DISPLAY_HEIGHT / 2 + 25
         and click[0] == 1):
        started = True

    # Draw stuff
    drawBackground()
    enemy_list.draw(gameDisplay)
    player_list.draw(gameDisplay)
    score.draw(gameDisplay)
    drawStartButton()
    pygame.display.update()
    clock.tick(15)

# Playing the game
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Update stuff
    enemy_list.update()
    for pipeSet in pipeSets:
        pipeSet.update()
    bird.checkCollision(enemy_list)
    bird.update(event)
    score.update()

    # Draw stuff
    drawBackground()
    enemy_list.draw(gameDisplay)
    player_list.draw(gameDisplay)
    score.draw(gameDisplay)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
