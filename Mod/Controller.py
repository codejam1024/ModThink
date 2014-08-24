from Mod import *
import sys
import readline
InitFuns = []
ExitFuns = []
Console_Prompt = ">"
Console_InputHook = None

def Welcome():
    print Mod.Config.GetConfig("system","soft", "name") + " by " + Mod.Config.GetConfig("system", "soft", "god")
    print "Version:" + Mod.Config.GetConfig("system", "soft", "version")

def ConsoleLoop():
    while True:
        if Console_InputHook != None:
            try:
                inputStr = raw_input(Console_Prompt)
                Console_InputHook(inputStr)
            except KeyboardInterrupt:
                Exit()
        else:
            break

def Init():
    Welcome()

    for func in InitFuns:
        func()

    ConsoleLoop()

def Exit():
    for func in ExitFuns:
        func()
    
    sys.exit(0)

