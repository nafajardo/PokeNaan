# Author: Nicholas Fajardo
# Date Created: 5/13/22

import pygame

class ScreenState:
    pass

# Responsible for navigating player to settings, livegame, or credits
# Cannot navigate back to itself
class MainMenu(ScreenState):
    def __init__(self):
        print("Main Menu Initialized")

    # Returns the PokeNaan Logo
    def Name(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("PokeNaan", True, (0, 255, 0), (0, 0, 255))
        textRect = text.get_rect()
        return textRect

# Responsible for adjusting the audio, video, and keybinds
class Settings(ScreenState):

    def setscreen(self):
        vs = self.getvideosettings()

        # Fullscreen mode
        if vs[2]:
            return pygame.display.set_mode(vs[0:1])
        # Windowed mode
        else:
            return pygame.display.set_mode(vs[0:1], pygame.FULLSCREEN)

    def getvideosettings(self):
        # TODO: Read from file and get video settings
        return (1920, 1080, True)

    def setvideosettings(self, width:int, height:int, fullscreen:bool):
        # TODO: Write to file video settings
        pass

class LiveGame(ScreenState):
    pass

class Credits(ScreenState):
    pass