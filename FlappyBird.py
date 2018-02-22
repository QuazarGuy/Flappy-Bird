import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

playing = True

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
