# Assets
import os
BASE_DIR = os.path.dirname(__file__)

# Join paths safely across all operating systems
SPRITESHEET_PATH = os.path.join(BASE_DIR, "Assets", "SpriteSheets", "Virus Game")

#Gravity settings
GRAVITY = 0.6

# Window Settings
WINDOW_WIDTH,WINDOW_HEIGHT = 960, 540

SPEED_HERO = 4
ANIMSPEED_HERO_DEFAULT = 0.25
ANIMSPEED_HERO_IDLE = 0.1

# speed of the virus
SPEED_VIRUS_RED = 2.1
SPEED_VIRUS_GREEN = 2.4
ANIMSPEED_VIRUS = 0.1
