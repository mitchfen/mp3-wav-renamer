''' TODO 
add mechanism to detect if sox is installed on Manjaro
    os.system("pacman -Q sox")
    then read in the bash output
-Sanitize user inputs - detect if they put mp3 or / or \
-Add functionality to move to sub directories within Music folder
-Add convenient way to count songs in directory and see progress working through them
-Add mechanism to keep file name the same
-Right now it assumes all files are mp3, need more code to deal with wav files
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
print (Fore.BLUE + "Directory: ", end = "")   # want input on same line, different color
print(Style.RESET_ALL, end = "")
musicDir = input()

#ensure directory is valid
# TODO: add code to confirm / at end of directory. This is critical
assert os.path.exists(musicDir), "ERROR "+str(musicDir) + " is an invalid directory"

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
        print(Fore.RED + "Renaming to " + inputName)    # want to confirm rename in red
        print(Style.RESET_ALL)
        cmd = ("mv " + files[i] + " " + inputName)
        os.system(cmd)

deinit() # per colorama documentation