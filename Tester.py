
def colortester():
    from Utilities.XML_Reader import ColorXML
    cm = ColorXML()
    cm.deleteColorByName("RED")
    cm.createColor("RED", 255, 0, 0)
    cm.deleteColorByName("WHITE")
    cm.deleteColorByRGB(0, 0, 0)
    cm.createColor("GREEN", 0, 255, 0)
    cm.saveColors()

if __name__=="__main__":
    colortester()