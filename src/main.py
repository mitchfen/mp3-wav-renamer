import os
import sys
import platform
import colorama
import re

# Import my own code
from getMusicDirectory import getMusicDirectory
from collectSongs import collectSongs
from rename import renamePrompt

def mainLoop(musicDir, files = []):

    # Loop throught the list, playing each file until keyboard interupt, then rename/keep/delete
    # Continue looping until each file in the list is handled then program terminates

    for i in range(len(files)):
        # I want the sox output to be yellow so I can distinguish from my python
        print (colorama.Fore.YELLOW)
        # need to wrap file names in quotes so they are read properly

        if platform.system() == 'Windows':
            #os.system("vlc --intf dummy " + "\"" + files[i] + "\"")
            #os.system('cls')
            print("Sorry, windows development ongoing... Not working yet")
            colorama.deinit() # need to stop colorama before exiting
            sys.exit()
        elif platform.system() =='Linux':
            #os.system('clear')
            os.system("play " + "\"" + files[i] + "\"")
        else:
            print("\nCannot determine OS, exiting...\n")
            colorama.deinit() # stop colorama before exiting
            sys.exit()

        # After keyboard interrupt:
        renamePrompt(i, files, musicDir)

    # If user has provided input on all songs in the list, the program exits here
    colorama.deinit() #stop colorama 

# Program control flow begins here
colorama.init() # per colorama documentation
musicDir = getMusicDirectory()
files = []
files = collectSongs(musicDir, files)
mainLoop(musicDir, files)
