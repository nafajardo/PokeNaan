# Author: Nicholas Fajardo
# Date Created: 5/19/22

import pygame
import numpy
from Utilities.SpriteSheet import SpriteSheet
from Utilities.OsTools import getcwd

def datamaptoimages(ss:SpriteSheet, map:numpy.ndarray):
    immap = []
    mapdims = map.shape
    ssdims = ss.getdims()
    for row in range(0, mapdims[0]):
        trow = []
        for col in range(0, mapdims[1]):
            item = int(map[row][col])
            spritepos = (int((item-1)/ssdims[0]+1), int((item-1)%ssdims[0]+1)) # Single Pos => SS Coordinate
            trow.append(ss.image_at_simple(spritepos[1], spritepos[0])) # Add image of sprite onto the map
        immap.append(trow)
    return immap

class Map:
    # Loads the file from storage
    def __init__(self, mapfile:str, spritesheetfile:str, spritesheetres:int = 16):
        self.res = spritesheetres
        self.ss = SpriteSheet(spritesheetfile, spritesheetres)
        self.map = numpy.loadtxt(getcwd()+"/Data/Maps/" + mapfile[0:-4] + "/" + mapfile, delimiter=",")
        self.imageset = datamaptoimages(self.ss, self.map)
        pass

    # Returns the width and height of the map (in pixels)
    def dims(self):
        return (self.map.shape[1]*self.res, self.map.shape[0]*self.res)

    # Return the image set
    def getimageset(self):
        return self.imageset

    def getimage(self, row, col):
        return self.imageset[row][col]