# requires sox to play music
# from my understanding the subprocess module is preferrable to os, but this works for now

''' TODO 
add mechanism to detect if sox is installed on Manjaro
    os.system("pacman -Q sox")
    then read in the bash output

Sanitize user inputs - detect if they put mp3 or / or \

Add functionality to move to sub directories within Music folder

Add convenient way to count songs in directory and see progress working through them

Add mechanism to keep file name the same
'''
import re
import os
import sys
import subprocess
from pathlib import Path
from colorama import Fore, init, Style
init() # colorama documentation says to init() colorama

# Ask user where the music is stored
print (Fore.GREEN + "\n\n\nHello, I will help you rename your music.")
print ("Please enter the directory your music is in.")
print ("Enter it like: /home/username/music\n")
print(Style.RESET_ALL)
musicDir = input("Directory:")

# Walk that directory and build array of files
files = []
#folders = []
for (path, dirnames, filenames) in os.walk(musicDir):
    #folders.extend(os.path.join(path, name) for name in dirnames)
    files.extend(os.path.join(path, name) for name in sorted(filenames))

# iterate through files array and use regex to replace " " with "\ " so we can navigate directories
for i in range (len(files)):
    tempString = str(files[i])
    files[i] = re.sub("\s", "\ ", tempString)

# play song until keyboard interupt
for i in range(len(files)):
    print (Fore.YELLOW) # I want the sox output to be yellow so I can distinguish from my python
    os.system("play " + files[i])
    print(Style.RESET_ALL)
    print ("\nKeyboard interupt detected\n")
    inputName = input("Name this file(x to delete): ")
    if inputName == "x":
            os.remove(files[i])
    else:
        inputName = musicDir + inputName + ".mp3"
        print (inputName)
        cmd = ("mv " + files[i] + " " + inputName)
        os.system(cmd)


deinit() # per colorama documentation