# Author: Nicholas Fajardo
# Date Created: 5/18/22

# Tests scale of objects
import random
import sys

import pygame

from Utilities.OsTools import getPrimaryMonitorResolution, getcwd
from Utilities.SpriteSheet import SpriteSheet
from Utilities.TextTools import textonbottom

def screenup(scale, resolution, screen):


    spriteres = 16
    ss = SpriteSheet(getcwd() + "/Art/16BitBasic/basictiles.png", spriteres)
    black = (0, 0, 0)
    screen.fill(black)
    for row in range(0, int(resolution[0] / (spriteres * scale))):
        for cell in range(0, int(resolution[1] / (spriteres * scale))):
            if row == 0 or row == int(resolution[0] / (spriteres * scale)) - 1 or cell == 0 or cell == int(
                    resolution[1] / (spriteres * scale)) - 1:
                im = ss.image_at_simple(1, 3)
            else:
                im = ss.image_at_simple(random.randint(1, int(ss.getbounds()[0] / spriteres)),
                                        random.randint(1, int(ss.getbounds()[1] / spriteres)))
            im = pygame.transform.scale(im, (spriteres * scale, spriteres * scale))
            imrect = im.get_rect()
            imrect.top = cell * (spriteres * scale)
            imrect.left = row * (spriteres * scale)
            screen.blit(im, imrect)

    screen.blit(
        *textonbottom("BLOCK SIZE: " + str(scale * spriteres) + " PIXELS" + " | SCALE: " + str(scale),
                      resolution[0], resolution[1], 16))
    pygame.display.flip()

def scaletester():
    pygame.init()
    scale = 5

    resolution = getPrimaryMonitorResolution()
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)

    while True:
        for event in pygame.event.get():

            # do other stuff
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                screenup(scale, resolution, screen)
                # Scale of 5 seems to work best
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scale = scale + 1
                elif event.key == pygame.K_DOWN and scale > 1:
                    scale = scale - 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                screenup(scale, resolution, screen)
                if event.button == 4:
                    scale = scale + 1
                elif event.button == 5 and scale > 1:
                    scale = scale - 1


if __name__=="__main__":
    scaletester()