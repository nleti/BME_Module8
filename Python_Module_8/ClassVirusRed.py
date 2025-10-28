import pygame
from Config import *
from ClassSpriteSheet import SpriteSheet

virusSprites = [
    (16,0,48,48),
    (80,0,48,48),
    (144,0,48,48),
    (208,0,48,48)
    ]


class VirusRed(pygame.sprite.Sprite):

    def __init__(self,position,moveRight):
        super().__init__()

        # Load spritesheet
        viruspath = os.path.join(SPRITESHEET_PATH, "Enemies","Virus_Red", "virus1_red.png")
        self.flySpriteSheet = SpriteSheet(os.path.join(viruspath),virusSprites)
        self.hitSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Attack/HitSheet.png", virusSprites)
        self.attackSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Attack/AttackSheet.png", virusSprites)

        #Gets image from directory 
        self.image = self.flySpriteSheet.getSprites(moveRight)[0]
        self.rect = self.image.get_rect(bottomleft = position)
        self.movingRight = moveRight
        self.yDir = 0
        self.animationIndex = 0
        self.currentState = "FLY"


    def update(self, level):
        # Update position
        if not self.movingRight:
            self.rect.x -= SPEED_VIRUS_RED
        else:
            self.rect.x += SPEED_VIRUS_RED

        # Turn around when leaving window bounds
        if self.rect.right < 0:
            self.movingRight = True
        elif self.rect.left > WINDOW_WIDTH:
            self.movingRight = False
        
        if self.currentState == 'DYING':
            self.yDir += GRAVITY
            self.rect.y += self.yDir
            if self.rect.top > WINDOW_HEIGHT:
                self.kill()

        #Trigger attack animation code:
        heroRect = level.hero.sprite.rect
        heroX = heroRect.centerx
        if self.currentState == 'FLY':
            if heroRect.top < self.rect.bottom <= heroRect.bottom:
                if self.movingRight == True:
                    if self.rect.left < heroX and self.rect.right > heroX - 50:
                        self.currentState = 'ATTACK'
                        self.animationIndex = 0
                    else:
                        if self.rect.right > heroX and self.rect.left < heroX + 50:
                            self.currentState = 'ATTACK'
                            self.animationIndex = 0
        elif self.currentState == 'ATTACK':
            if self.movingRight == True:
                if self.rect.left >= heroX or self.rect.right < heroX - 50:
                    self.currentState = 'FLY'
                    self.animationIndex = 0 
                else:
                    if self.rect.right <= heroX or self.rect.left > heroX + 50:
                        self.currentState = 'FLY'
                        self.animationIndex = 0

        # Select animation for current state
        self.selectAnimation()

        # Animate sprite
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            if self.currentState == 'ATTACK' or self.currentState == 'DYING':
                self.animationIndex = len (self.currentAnimation) -1
            else:
                self.currentState = 'FLY'
                self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_VIRUS
        if self.currentState == "FLY":
            self.currentAnimation = self.flySpriteSheet.getSprites(flipped = self.movingRight)
        elif self.currentState == 'ATTACK':
            self.animationSpeed = ANIMSPEED_VIRUS_ATTACK
            self.currentAnimation = self.attackSpriteSheet.getSprites(flipped = self.movingRight)
        else:
              self.currentAnimation = self.hitSpriteSheet.getSprites(flipped = self.movingRight)

    def die(self):
        if self.currentState != "DYING":
            self.animationIndex = 0
            self.currentState = 'DYING'

