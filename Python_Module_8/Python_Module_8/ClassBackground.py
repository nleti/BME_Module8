import pygame
from Config import *

class Background():
    
    def __init__(self):
        background_path = os.path.join(SPRITESHEET_PATH, "Background", "BackgroundV2.png")

        # Load and scale
        self.skyImage = pygame.image.load(background_path).convert()
        self.skyImage = pygame.transform.scale(self.skyImage,(WINDOW_WIDTH,WINDOW_HEIGHT))

    def draw(self,displaySurface):
        displaySurface.blit(self.skyImage,(0,0))

