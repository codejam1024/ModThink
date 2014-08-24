from Mod import *

def InputHook(inputStr):
    print "Your input:%s" % inputStr

def Init():
    print "I am Test Module"
    Mod.Controller.Console_InputHook =  InputHook
