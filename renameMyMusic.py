''' TODO 
add mechanism to detect if sox is installed on Manjaro
    os.system("pacman -Q sox")
    then read in the bash output
-Sanitize user inputs - detect if they include .mp3 or slashes
-Fix issues dealing with files which have unexpected characters like () or #
-Add functionality to move to sub directories within Music folder
-Add convenient way to count songs in directory and see progress working through them
-Right now it assumes all files are mp3, need more code to deal with wav files
'''

import re
import os
import sys
import subprocess
from pathlib import Path
from colorama import Fore, Style

# Ask user where the music is stored
print (Fore.GREEN + "\nHello, I will help you rename your music.")
print ("Please enter the directory your music is in.")
print ("Enter it like: /home/username/music\n")
print(Style.RESET_ALL)
print (Fore.BLUE + "Directory: ", end = "")   # want input on same line, different color
print(Style.RESET_ALL, end = "")
musicDir = input()

#Ensure directory is valid and ends in a backslash
if musicDir[len(musicDir)-1] != "/":
    musicDir += "/"
assert os.path.exists(musicDir), "ERROR "+str(musicDir) + " is an invalid directory"

# Walk that directory and build array of files
files = []
for (path, dirnames, filenames) in os.walk(musicDir):
    files.extend(os.path.join(path, name) for name in sorted(filenames))

# Iterate through files array and use regex to replace " " with "\ " so we can navigate directories
# Example: /home/mitch/music/song\ with\ spaces.mp3
for i in range (len(files)):
    tempString = str(files[i])
    files[i] = re.sub("\s", "\ ", tempString)

# Play song until keyboard interupt
for i in range(len(files)):
    print (Fore.YELLOW) # I want the sox output to be yellow so I can distinguish from my python
    os.system("play " + files[i])
    print(Style.RESET_ALL)
    inputName = input("Name this file(x to delete, k to keep): ")
    if inputName == "x":
            #os.remove(files[i])    This fails when file name has spaces, unsure why
            cmd = ("rm " + files[i])
            os.system(cmd)      # this is always successful, albiet with risky rm command
            print(Fore.RED + "Deleted.")
            print(Style.RESET_ALL)
    elif inputName == "k":
            print(Fore.RED + "Keeping file as " + files[i])
            print(Style.RESET_ALL)
    else:
        inputName = musicDir + inputName + ".mp3"
        print(Fore.RED + "Renaming to " + inputName)    # want to confirm rename in red
        print(Style.RESET_ALL)
        cmd = ("mv " + files[i] + " " + inputName)
        os.system(cmd)