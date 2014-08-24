import os
import sys
import time
s = os.sep
class Mod():
    pass

def ModInit():
    global Mod
    Mod.Modules = []
    for f in os.listdir('Mod'):
        if os.path.isfile('Mod' + s + f):
            fname = os.path.splitext(f)
            if fname[1] == '.py' and fname[0] != '__init__':
                __import__('Mod.'+fname[0])
                #print '[-]Load Mod.' + fname[0]
                if fname[0] != "Controller":
                    Mod.Modules.append(fname[0])
                exec 'Mod.' + fname[0] + "=" + fname[0]

    Mod.Modules.append("Controller")

    for m in Mod.Modules:
        if m != "Controller":
            try:
                exec 'Mod.' + m + '.Init()'
            except:
                pass

    Mod.Controller.Init()

ModInit()

