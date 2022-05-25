# Author: Nicholas Fajardo
# Date Created: 5/25/22
import sys

from Utilities.MapLoader import Map
from Utilities.OsTools import getcwd
import pygame

from Utilities.PyGameCustom import Screen
from Utilities.SpriteSheet import SpriteSheet


def main():
    scale = 7
    screen = Screen(fullscreen=True)
    res = screen.getresolution()
    testmap = Map("TestGround.csv", getcwd() + "/Art/16BitBasic/basictiles.png")
    images = testmap.getimageset()
    dims = testmap.dims()
    resolution = 16
    '''
    ss = SpriteSheet(getcwd() + "/Art/16BitBasic/characters.png", resolution)
    player = pygame.transform.scale(ss.image_at_simple(8, 5), (resolution * scale, resolution * scale))'''
    player = pygame.transform.scale(pygame.image.load(getcwd()+"/Art/16BitBasic/Villain.png"), (resolution * scale^2, resolution * scale^2))

    playerrect = player.get_rect()
    playerrect.center = (res[0]/2, res[1]/2)

    speed = 4*scale
    curspeed = [0, 0]

    while True:
        screen.fillscreen((0, 0, 0))
        cp = [int((res[0] - dims[0] * scale) / 2 + curspeed[0]), int((res[1] - dims[1] * scale) / 2 + curspeed[1])]
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            curspeed[1] += speed
        if keys[pygame.K_s]:
            curspeed[1] += speed*-1
        if keys[pygame.K_a]:
            curspeed[0] += speed
        if keys[pygame.K_d]:
            curspeed[0] += speed*-1
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

        for row in range(0, len(images)):
            cp0ref = cp[0]
            for col in range(0, len(images[0])):
                image = testmap.getimage(row, col)
                image = pygame.transform.scale(image, (resolution * scale, resolution * scale))
                imagerect = image.get_rect()
                imagerect.topleft = (cp[0]+curspeed[0], cp[1])
                screen.updateimage(image, imagerect)
                cp[0] = cp[0] + resolution * scale
            cp[1] = cp[1] + resolution * scale
            cp[0] = cp0ref

        screen.updateimage(player, playerrect)

        screen.frameflip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__=="__main__":
    main()