import pygame
from Config import *
from ClassSpriteSheet import SpriteSheet

runSprties = [
    (24, 16, 40, 52),
    (104, 16, 40, 52),
    (184, 16, 40, 52),
    (264, 16, 40, 52),
    (344, 16, 40, 52),
    (424, 16, 40, 52),
    (504, 16, 40, 52),
    (584, 16, 40, 52)
]

idleSprites = [
    (12, 12, 44, 52),
    (76, 12, 44, 52),
    (140, 12, 44, 52),
    (204, 12, 44, 52)
 ]

attackSprites = [
    (4, 0, 92, 80),
    (100, 0, 92, 80),
    (196,0, 92, 80),
    (294, 0, 92, 80),
    (388,0, 92, 80),
    (484, 0, 92, 80),
    (580, 0, 92, 80),
    (676, 0, 92, 80)
]

deathSprites = [
    (0, 0, 64, 56),
    (80, 0, 64, 56),
    (160, 0, 64, 56),
    (240, 0, 64, 56),
    (320, 0, 64, 56),
    (400, 0, 64, 56),
    (480, 0, 64, 56),
    (560, 0, 64, 56)
]

class Hero(pygame.sprite.Sprite):

    def __init__(self, position, faceRight):
        super().__init__()

        # Load Sprites
        # Paths to get the character animations
        idlepath = os.path.join(SPRITESHEET_PATH, "Character","Idle", "Idle-Sheet.png")
        runpath = os.path.join(SPRITESHEET_PATH, "Character","Run","Run-Sheet.png")
        runattack = os.path.join(SPRITESHEET_PATH, "Character","Attack","AttackSheet.png")

        idleSpriteSheet = SpriteSheet(idlepath, idleSprites)
        runSpriteSheet = SpriteSheet(runpath, runSprties)
        attackSpriteSheet = SpriteSheet(runattack, attackSprites)
        deathSpriteSheet = SpriteSheet(deadattack, deathSprites)

        self.spriteSheets = {
            'IDLE' : idleSpriteSheet,
            'RUN' : runSpriteSheet,
            'ATTACK' : attackSpriteSheet
            'DIE' : deathSpriteSheet
        }

        self.animationIndex = 0
        self.facingRight = faceRight
        self.currentState = 'IDLE'
        self.xDir = 0
        self.speed = SPEED_HERO
        self.xpos = position[0]
        self.ypos = position[1]


    def update(self, level):

        self.previousState = self.currentState
        self.xDir = 0

        if self.currentState != 'ATTACK' and self.currentState != 'DIE':
            keys =pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.currentState = 'ATTACK'
            elif keys[pygame.K_a]:
                self.xDir = -1
                self.facingRight = False
                self.currentState = 'RUN'
            elif keys[pygame.K_d]:
                self.xDir = 1
                self.facingRight = True
                self.currentState = 'RUN'
            else:
                self.currentState = 'IDLE'

        #Selecting animation for current player action (idle, run, jup, fall, etc.):
        self.selectAnimation()

        #Start from beginning of a new animation:
        if self.previousState != self.currentState:
            self.animationIndex = 0

        #Select the image:
        self.image = self.currentAnimation[int(self.animationIndex)]

        #Select a rect size depending on the current animation:
        #(xPos, yPos) = bottom-center position of the Sprite:
        if self.currentState == 'IDLE':
            self.rect = pygame.Rect(self.xpos - 22, self.ypos - 52, 44, 52)
        elif self.currentState == 'RUN':
            self.rect = pygame.Rect(self.xpos - 20, self.ypos - 48, 40, 48)
        elif self.currentState == 'ATTACK':
            self.rect =pygame.Rect(self.xpos - 44, self.ypos - 64, 88, 64)
        elif self.currentState == 'DIE':
            self.rect =pygame.Rect(self.xpos - 32, self.ypos - 48, 64, 48)


        self.image = self.currentAnimation[int(self.animationIndex)]

        if self.currentState == 'IDLE':
            self.rect = pygame.Rect(self.xpos - 22, self.ypos - 52, 44, 52)

        #Play animation until end of current animation is reached:
        self.animationIndex += self.animationspeed
        if self.animationIndex >= len(self.currentAnimation):
            if self.currentState == 'DIE':
                self.animationIndex = len(self.currentAnimation) - 1
            else:
                self.animationIndex = 0
                self.currentState = 'IDLE'

        self.moveHorizontal(level)
        self.checkEnemyCollisions(level.virusesRed)

    def selectAnimation(self):
        self.animationspeed = ANIMSPEED_HERO_DEFAULT
        if self.currentState == 'IDLE':
            self.animationspeed = ANIMSPEED_HERO_IDLE

        spriteSheet = self.spriteSheets[self.currentState]
        self.currentAnimation = spriteSheet.getSprites(flipped = not self.facingRight)


    def moveHorizontal(self, level):
        self.rect.centerx += self.xDir * self.speed

        #Do not walk outsie level:
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        self.xpos = self.rect.centerx

    #Dying function:
    def die(self):
        if self.currentState != 'DIE':
            self.currentState = 'DIE'
            self.animationIndex = 0


    def checkEnemyCollisions(self, enemies):
        collidedSprites = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in collidedSprites:
            if self.currentState == 'ATTACK':
                if self.facingRight == True:
                    if enemy.rect.left < self.rect.right - 30:
                        enemy.die()
                else:
                    if enemy.rect.right > self.rect.left + 30:
                        enemy.die()
            else:
                if enemy.currentState != 'DYING':
                    if self.rect.left < enemy.rect.left:
                        if self.rect.right > enemy.rect.left + 16:
                            self.die()
                    elif self.rect.right > enemy.rect.right:
                        if self.rect.left < enemy.rect.right - 16:
                            self.die()