# Author: Nicholas Fajardo
# Date Created: 5/18/22
import sys

import pygame.event
from pygame import mixer
from Utilities.OsTools import getcwd, getPrimaryMonitorResolution
from Utilities.TextTools import textonbottom

mixer.init()
mixer.music.load(getcwd() + "/Sounds/Ambient/RandomSong.mp3")
volume = 3
mixer.music.play()
mixer.music.set_volume(volume)
pygame.init()
resolution = 900, 128
screen = pygame.display.set_mode(resolution)
playing = True
currtime = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            mixer.music.stop()
            sys.exit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and volume < 10:
                volume = volume + 1
                mixer.music.set_volume(volume*0.1)
            if event.key == pygame.K_DOWN and volume > 0:
                volume = volume - 1
                mixer.music.set_volume(volume*0.1)
            if event.key == pygame.K_p and playing:
                mixer.music.pause()
                playing = not playing
            elif event.key == pygame.K_p and not playing:
                mixer.music.unpause()
                playing = not playing
        screen.fill((0, 0, 0))
        screen.blit(*textonbottom("VOLUME: " + str(volume*10), resolution[0], resolution[1], resolution[1]))
        pygame.display.flip()