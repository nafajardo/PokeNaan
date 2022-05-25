# Author: Nicholas Fajardo
# Date Created: 5/18/22
import pygame
from Utilities.OsTools import getPrimaryMonitorResolution

class Screen:
    def __init__(self, width:int = None, height:int = None, fullscreen=False):
        if width == None and height == None:
            res = getPrimaryMonitorResolution()
        else:
            res = width, height
        self.width = res[0]
        self.height = res[1]
        self.boot(self.width, self.height, fullscreen)

    def getresolution(self):
        return (self.width, self.height)

    def boot(self, width:int, height:int, fullscreen):
        #TODO boot the game, with certain resolution and fullscreen mode in mind
        pygame.init()
        if fullscreen:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))
        return self.screen

    def frameflip(self):
        pygame.display.flip()

    def fillscreen(self, RGB=(0, 0, 0)):
        self.screen.fill(RGB)

    def updateimage(self, image, imagerect):
        self.screen.blit(image, imagerect)