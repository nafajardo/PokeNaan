# Author: Nicholas Fajardo
# Date Created: 5/18/22
# Testing movable character speeds
import sys

import pygame.event

from Utilities.PyGameCustom import Screen
from Utilities.SpriteSheet import SpriteSheet
from Utilities.OsTools import getcwd

screen = Screen(720, 480)
resolution = screen.getresolution()
spriteres = 16
ss = SpriteSheet(getcwd()+"/Art/16BitBasic/characters.png", spriteres)
scale = 5
player = pygame.transform.scale(ss.image_at_simple(8, 5), (spriteres * scale, spriteres * scale))
playerrect = player.get_rect()
playercoord = [0, 0] # Top Left
movementscale = spriteres*scale # Set to spriteres for correct movement
while True:
    for event in pygame.event.get():
        speed = [0, 0]
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if playercoord[1] != 0:
                    speed[1] = -1
                player = pygame.transform.scale(ss.image_at_simple(8, 8), (spriteres * scale, spriteres * scale))
            if event.key == pygame.K_s:
                if playercoord[1] != resolution[1]-movementscale:
                    speed[1] = 1
                player = pygame.transform.scale(ss.image_at_simple(8, 5), (spriteres * scale, spriteres * scale))
            if event.key == pygame.K_a:
                if playercoord[0] != 0:
                    speed[0] = -1
                player = pygame.transform.scale(ss.image_at_simple(7, 6), (spriteres * scale, spriteres * scale))
            if event.key == pygame.K_d:
                if playercoord[0] != resolution[0]-movementscale:
                    speed[0] = 1
                player = pygame.transform.scale(ss.image_at_simple(7, 7), (spriteres * scale, spriteres * scale))
        playercoord = [playercoord[0] + speed[0]*movementscale, playercoord[1] + speed[1]*movementscale]
        playerrect.top = playercoord[1]
        playerrect.left = playercoord[0]
        screen.fillscreen()
        screen.updateimage(player, playerrect)
        screen.frameflip()
