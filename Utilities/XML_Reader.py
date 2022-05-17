# Author: Nicholas Fajardo
# Date Created: 5/13/22

# Assuming the data structure outlined in the README for our items, this class has
import xml.etree.ElementTree as elt
from Utilities.Errors import IncorrectInput

# Load, Read, Write, and Save colors
class ColorXML:
    def __init__(self):
        self.colordir = "Data/Colors.xml"
        self.loadColors()

    # Returns a dictionary with all the colors from the XML file
    def loadColors(self):
        tree = elt.parse(self.colordir)
        root = tree.getroot()
        self.colors = {color.attrib['id']:(int(color[0].text), int(color[1].text), int(color[2].text)) for color in root}
        return True

    # Returns the RGB values of a color
    def getColorValue(self, name:str):
        return self.colors[name]

    def createColor(self, name:str, rVal:int, gVal:int, bVal:int, reassign:bool=False):
        """Creates a new color to use

        Keyword arguments:
        name -- The name of the color (3-10 characters, alphas only)
        rVal -- red Value (0,255 inclusive)
        gVal -- green Value (0,255 inclusive)
        bVal -- blue Value (0,255 inclusive)
        """
        # Error handling
        if self.colors is None or name in self.colors.keys():
            raise IncorrectInput("Color must be new (Name Exists)")
        if len(name) not in range(3, 11) or not name.isalpha():
            raise IncorrectInput("Color name must be 3-10 characters long, and only AlphaNumerics")
        if rVal not in range(0, 256) or gVal not in range(0, 256) or bVal not in range(0, 256):
            raise IncorrectInput("Colors must be between 0 - 255 each")
        # If we want to reassign the color if it exists already based on its value
        if (rVal, gVal, bVal) in list(self.colors.values()) and reassign:
            # Delete the color
            for k, v in self.colors:
                if v == (rVal, gVal, bVal):
                    del self.colors[k]
                    break
            self.colors.update({name, (rVal, gVal, bVal)})
        else:
            self.colors[name] = (rVal, gVal, bVal)

    # Save Colors into XML file
    def saveColors(self):
        tree = elt.ElementTree()
        colors = elt.Element("Colors")

        for colorname in list(self.colors.keys()):
            color = elt.Element("Color")
            color.attrib = {"id":colorname}
            r = elt.Element("R")
            r.text = str(self.colors[colorname][0])
            g = elt.Element("G")
            g.text = str(self.colors[colorname][1])
            b = elt.Element("B")
            b.text = str(self.colors[colorname][2])
            color.append(r)
            color.append(g)
            color.append(b)
            colors.append(color)

        tree._setroot(colors)
        tree.write(self.colordir)

    def deleteColorByName(self, name:str):
        try:
            del self.colors[name]
            return True
        except:
            return False

    def deleteColorByRGB(self, R:int, G:int, B:int):
        try:
            for color in list(self.colors.keys()):
                if self.colors[color] == (R, G, B):
                    del self.colors[color]
                    break
            return True
        except:
            return False

# Load, Read, Write, and Save PokeNaan
class PokeNaanXML:
    # TODO
    pass