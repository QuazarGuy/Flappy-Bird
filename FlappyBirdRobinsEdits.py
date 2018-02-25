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
PIPE_GAP = 360 + 40  # no gap = 360

# variables for the bird moving
y = 210
y_change = 0  # how fast the bird is moving THIS FRAME
y_upRate = 5  # the max speed we want the bird to go up
y_downRate = -5  # the max speed fast we want the bird to go down
spacePressed = False  # this variable will tell the while playing loop the space bar was recently pressed and the bird
# should go up for a bit
framesPerJump = 5  # this variable is for how many frames after the space bar is pressed that we want it to move up
# before it starts to move down again. I imagine it'll probably have to be tweaked.
jumpFramesCounter = 0  # how long the bird has actually jumped

# variables for score counting
# NOTE: All of this'll have to be tweaked; for now it's just the framework that'll ...probably give the player
# a lot of points.
framesForPoint = 90  # number of frames before point is awarded
sinceLastPointCounter = 0  # how many frames it's been since the last point was awarded
pointCounter = 0  # the number of points the player has

# variables for start button
startPressed = False


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
    gameDisplay.blit(birdImg, (50, y))


def drawScore(counter):
    font = pygame.font.SysFont(None, 20, False)
    text = font.render("Score: "+str(counter), True, (0, 0, 0))
    gameDisplay.blit(text, (3, 3))

def drawStart():
    pygame.draw.rect(gameDisplay, (255, 255, 255), ((display_width-200)/2, (display_height-50)/2, 200, 50))
    font = pygame.font.SysFont(None, 50, False)
    text = font.render("Start!", True, (0, 0, 0))
    gameDisplay.blit(text, (180, 190))


def notStarted(started):

    while started == False:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (display_width-200)/2 + 200 > mouse[0] > (display_width-200)/2 and (display_height-50)/2 + 50 > mouse[1] > (display_height-50)/2 and click[0] == 1:
            started = True

        drawBackground()
        drawPipes(PIPE_DISTANCE, PIPE_GAP)
        drawGround()
        drawBird(y)
        drawScore(pointCounter)
        drawStart()
        pygame.display.update()
        clock.tick(15)


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    # Do stuff

    notStarted(startPressed)
    startPressed = True

    # bird jumps up
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if framesPerJump != jumpFramesCounter:
                spacePressed = True
                jumpFramesCounter = framesPerJump  # resets the jump and jump speed
            # else do nothing
    if spacePressed == True:
        if jumpFramesCounter != 0:
            y_change = y_upRate - (framesPerJump - jumpFramesCounter)  # this makes it lose speed as it goes up
            jumpFramesCounter = jumpFramesCounter - 1
        if jumpFramesCounter == 0:  # the jump is over
            spacePressed = False

    if spacePressed == False:  # the bird is going down now
        if y_change != y_downRate:
            y_change = y_change - 1  # this makes it slowly gain speed again going down

    y = y - y_change

    # this'll be used to make the game quit if flappy hits the top or bottom of the screen. For testing purposes I've
    # got it set so right now he just stops moving.
    if y >= 300:  # ground distance
        y = 300
    #    quit()

    if y <= -2:  # highest spot
        y = -2
    #    quit()

    # testing code:

    # player gets points
    if sinceLastPointCounter < framesForPoint:
        sinceLastPointCounter = sinceLastPointCounter + 1

    if sinceLastPointCounter >= framesForPoint:
        pointCounter = pointCounter + 1
        sinceLastPointCounter = 0  # resents the counter until next point

    # Draw stuff
    drawBackground()
    drawPipes(PIPE_DISTANCE, PIPE_GAP)
    drawGround()
    drawBird(y)
    drawScore(pointCounter)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
