import pygame
from Config import *
from ClassSpriteSheet import SpriteSheet

virusSprites = [
    (16,0,48,48),
    (80,0,48,48),
    (144,0,48,48),
    (208,0,48,48)
    ]


class VirusGreen():

    def __init__(self,position,moveRight):
        # Load spritesheet
        viruspathgreen = os.path.join(SPRITESHEET_PATH, "Enemies","Virus_Green", "virus_green.png")
        self.flySpriteSheet = SpriteSheet(os.path.join(viruspathgreen),virusSprites)


        #Gets image from directory 
        self.image = self.flySpriteSheet.getSprites(moveRight)[0]
        self.rect = self.image.get_rect(bottomleft = position)
        self.movingRight = moveRight

        self.animationIndex = 0
        self.currentState = "FLY"


    def update(self, level):
        # Update position
        if not self.movingRight:
            self.rect.x -= SPEED_VIRUS_GREEN
        else:
            self.rect.x += SPEED_VIRUS_GREEN

        # Turn around when leaving window bounds
        if self.rect.right < 0:
            self.movingRight = True
        elif self.rect.left > WINDOW_WIDTH:
            self.movingRight = False

        # Select animation for current state
        self.selectAnimation()

        # Animate sprite
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]

    def draw(self,displaySurface):
        displaySurface.blit(self.image,self.rect)
        pass

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_VIRUS
        if self.currentState == "FLY":
            self.currentAnimation = self.flySpriteSheet.getSprites(flipped = self.movingRight)

