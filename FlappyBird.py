import pygame
from random import randint

pygame.init()

display_width = 460
display_height = 410

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
playing = True

# Load Images
background = pygame.image.load('assets\\bg.png')
ground = pygame.image.load('assets\\ground.png')
upperPipe = pygame.image.load('assets\\tube1.png')
lowerPipe = pygame.image.load('assets\\tube2.png')
birdImg = pygame.image.load('assets\\bird_sing.png')

PIPE_DISTANCE = 150
PIPE_GAP = 360 + 40             # no gap = 360

def drawBackground():
    gameDisplay.blit(background, (0, -10))
    gameDisplay.blit(background, (288, -10))

# Probably going to make a class for pipes
def pipePair(pipeGap, x, y):
    gameDisplay.blit(upperPipe, (x, y))
    gameDisplay.blit(lowerPipe, (x, y + pipeGap))

def drawPipes(pipeDistance, pipeGap):
    pipePair(pipeGap, 230, -160)
    pipePair(pipeGap, 230 + pipeDistance, -160)

def drawGround():
    gameDisplay.blit(ground, (0, 320))
    gameDisplay.blit(ground, (336, 320))

def drawBird(y):
    gameDisplay.blit(birdImg, (50, 210))

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
# Do stuff

# Draw stuff
    drawBackground()
    drawPipes(PIPE_DISTANCE, PIPE_GAP)
    drawGround()
    drawBird(0)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
