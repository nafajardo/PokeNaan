# Author: Nicholas Fajardo
# Date Created: 5/17/22

import time, sys, os
from Utilities import Errors
import pygame
from Utilities.OsTools import getcwd, getPrimaryMonitorResolution
from Utilities.TextTools import textonbottom

# Sprite Sheet Object retrieval
class SpriteSheet(object):
    def __init__(self, filename:str, res:int):
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.res = res
        except pygame.error as message:
            print('Unable to load spritesheet image:' + filename)
            raise SystemExit(message)

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

# Tests scale of objects
def scaletester():
    pygame.init()

    spriteres = 16
    resolution = getPrimaryMonitorResolution()
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    ss = SpriteSheet(getcwd() + "/Art/16BitBasic/basictiles.png", spriteres)
    scale = 5
    black = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scale = scale + 1
                elif event.key == pygame.K_DOWN and scale > 1:
                    scale = scale - 1
            screen.fill(black)
            for row in range(0, int(resolution[0] / (spriteres * scale))):
                for cell in range(0, int(resolution[1] / (spriteres * scale))):
                    if row == 0 or row == int(resolution[0] / (spriteres * scale))-1 or cell == 0 or cell == int(resolution[1] / (spriteres * scale))-1:
                        im = ss.image_at_simple(1, 3)
                    else:
                        im = ss.image_at_simple(1, 10)
                    im = pygame.transform.scale(im, (spriteres * scale, spriteres * scale))
                    imrect = im.get_rect()
                    imrect.top = cell * (spriteres * scale)
                    imrect.left = row * (spriteres * scale)
                    screen.blit(im, imrect)

            screen.blit(*textonbottom("BLOCK SIZE: " + str(scale*spriteres) + " PIXELS" + " | SCALE: " + str(scale) , resolution[0], resolution[1], 16))
            pygame.display.flip()

            # Scale of 5 seems to work best

if __name__=="__main__":
    scaletester()