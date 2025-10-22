from shutil import move
import pygame
from Config import *
from ClassHero import Hero
from ClassBackground import Background
from ClassVirusRed import VirusRed
from ClassVirusGreen import VirusGreen

class Level():
    def __init__(self,displaySurface):

        self.background = Background()
        # sets position of the virus and where it is 
        
        self.hero = Hero((400, 400), faceRight = True)
        # Red viruses
        self.virus1 = VirusRed((200,200),moveRight = True)
        self.virus12 = VirusRed((300,300),moveRight = False)
        
        #Green virus
        self.virus_g = VirusGreen((500,500),moveRight = True)
        self.virus_g2 = VirusGreen((100,100),moveRight = False)

        self.displaySurface = displaySurface


    def update(self):
        self.hero.update(self)

        # Red virus
        self.virus1.update(self)
        self.virus12.update(self)

        # Green virus
        self.virus_g.update(self)
        self.virus_g2.update(self)
       

    def draw(self):
        self.background.draw(self.displaySurface)

        self.hero.draw(self.displaySurface)

        # Drawing red virus
        self.virus1.draw(self.displaySurface)
        self.virus12.draw(self.displaySurface)

        # Green virus
        self.virus_g.draw(self.displaySurface)
        self.virus_g2.draw(self.displaySurface)


    def run(self):
        self.update()
        self.draw()



