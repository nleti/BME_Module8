from math import e
import pygame
from Config import *
from ClassLevel import Level


# Initialise pygame
pygame.init()
clock = pygame.time.Clock() #used to limit framerate 

# Open Window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Virus Attack")

level = Level(displaySurface)


isGameRunning = True
while isGameRunning:
    #Handles events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGameRunning = False

    level.run()

    pygame.display.flip()
    clock.tick(60)

# After game closed,close pygame
pygame.quit()
