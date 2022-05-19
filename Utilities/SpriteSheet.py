# Author: Nicholas Fajardo
# Date Created: 5/17/22

from Utilities import Errors
import pygame

# Sprite Sheet Object retrieval
class SpriteSheet(object):
    def __init__(self, filename:str, res:int):
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.res = res
            self.bounds = (self.sheet.get_rect().right, self.sheet.get_rect().bottom)
        except pygame.error as message:
            print('Unable to load spritesheet image:' + filename)
            raise SystemExit(message)

    def getbounds(self):
        return self.bounds

    # Load a specific image from a specific rectangle
    # EX: 1, 1 is the first left image (Top Left is origin of graph), with a resolution of 16
    def image_at_simple(self, x:int, y:int):
        raw_x = (x-1)*self.res
        raw_y = (y-1)*self.res
        sheetrect = self.sheet.get_rect()
        if raw_x >= sheetrect.right-self.res+1 or raw_y >= sheetrect.bottom-self.res+1:
            raise Errors.IncorrectInput("Selected coordinate is out of range")
        imagerect = pygame.Rect(raw_x, raw_y, self.res, self.res)
        image = pygame.Surface(imagerect.size).convert().convert_alpha()
        image.blit(self.sheet, (0, 0), imagerect)
        return image