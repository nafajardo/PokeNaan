# Author: Nicholas Fajardo
# Date Created: 5/17/22

import pygame
from Utilities.OsTools import getcwd

# TODO textrender()

def textonbottom(text:str, width:int, height:int, fontsize=32):
    font = pygame.font.Font(getcwd()+"/Fonts/VCR_Font.ttf", fontsize)
    text = font.render(text, True, (255, 255, 255))
    #text.set_alpha(127)
    textrect = text.get_rect()
    textrect.bottom = (height)
    textrect.left = width/2 - textrect.size[0]/2
    return (text, textrect)