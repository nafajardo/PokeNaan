import pygame

from ScreenStates import MainMenu, Settings, LiveGame, Credits

# Game States
mm = MainMenu()
settings = Settings()
lg = LiveGame()
credits = Credits()

# Spawn the screen
screen = settings.setscreen()

states = ('Main Menu', 'Settings', 'Live Game', 'Credits')

# Game Frame Loop
while True:
    pass