import pygame

from ScreenStates import MainMenu, Settings, LiveGame, Credits
from Utilities.PyGameCustom import Screen

mm = MainMenu()
settings = Settings()
lg = LiveGame()
credits = Credits()

# Spawn the screen
screen = Screen()

states = ('Main Menu', 'Settings', 'Live Game', 'Credits')

# Game Frame Loop
while True:
    pass