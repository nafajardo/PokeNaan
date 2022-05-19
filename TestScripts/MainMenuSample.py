# Author: Nicholas Fajardo
# Date Created: 5/18/22
import sys

import pygame.event

from Utilities.OsTools import getcwd
from Utilities.PyGameCustom import Screen

screen = Screen(fullscreen=True)
screen.fillscreen()
res = screen.getresolution()
pygame.mouse.set_visible(False)
scale = 2
res = 16
cursor = pygame.transform.scale(pygame.image.load(getcwd() + "/Art/Cursor.png").convert().convert_alpha(), (res*scale,res*scale))
cursorrect = cursor.get_rect()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            sys.exit()

    screen.fillscreen()

    cursorrect.center = pygame.mouse.get_pos()
    screen.updateimage(cursor, cursorrect)
    pygame.display.flip()