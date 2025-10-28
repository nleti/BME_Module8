from shutil import move
import pygame
from Config import *
from ClassHero import Hero
from ClassBackground import Background
from ClassVirusRed import VirusRed
from ClassVirusGreen import VirusGreen

class Level():
    def __init__(self,displaySurface):

        #Creating groups:
        self.background = Background()
        self.hero = pygame.sprite.GroupSingle()
        self.virusesRed = pygame.sprite.Group()
        self.virusesGreen = pygame.sprite.Group()

        # sets position of the virus and where it is 

        self.hero.add(Hero((400, 400), faceRight = True))

        # Red viruses
        self.virusesRed.add(VirusRed((200,200),moveRight = True))
        self.virusesRed.add(VirusRed((300,300),moveRight = False))
        
        #Green virus
        self.virusesGreen.add(VirusGreen((500,500),moveRight = True))
        self.virusesGreen.add(VirusGreen((100,100),moveRight = False))

        self.displaySurface = displaySurface


    def update(self):
        self.hero.update(self)

        # Red virus
        self.virusesRed.update(self)

        # Green virus
        self.virusesGreen.update(self)
       

    def draw(self):
        self.background.draw(self.displaySurface)

        self.hero.draw(self.displaySurface)

        # Drawing red virus
        self.virusesRed.draw(self.displaySurface)

        # Green virus
        self.virusesGreen.draw(self.displaySurface)


    def run(self):
        self.update()
        self.draw()



