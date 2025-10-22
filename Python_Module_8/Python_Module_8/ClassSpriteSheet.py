import pygame
from Config import *

class SpriteSheet():

    def __init__(self,spriteSheetPath, spritePositions):
        # this is so we can get the animations of the virus, if it is going other way around then it flips it
        image = pygame.image.load(spriteSheetPath).convert_alpha()
        self.sprites = []
        self.spritesFlipped = []

        for position in spritePositions:
            sprite = image.subsurface(pygame.Rect(position))
            self.sprites.append(sprite)
            sprite = pygame.transform.flip(sprite,True,False)
            self.spritesFlipped.append(sprite)

    def getSprites(self,flipped):
        if flipped == True:
            return self.spritesFlipped

        else:
            return self.sprites