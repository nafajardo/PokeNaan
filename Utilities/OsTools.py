# Author: Nicholas Fajardo
# Date Created: 5/17/22

import os
from screeninfo import get_monitors

def getcwd():
    cwd = os.getcwd()
    return cwd[0:cwd.index("PokeNaan")+len("PokeNaan")]

def getPrimaryMonitorResolution():
    for monitor in get_monitors():
        if monitor.is_primary: return (monitor.width, monitor.height)