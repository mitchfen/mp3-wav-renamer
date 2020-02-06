# requires sox to play music
# requires Python 3.5 or higher for subprocess.run function
import re
import os
import subprocess
from pathlib import Path

''' TODO use subprocess to ensure sox is installed
add mechanism to detect if sox is installed on Manjaro
os.system("pacman -Q sox")
subprocess.check_output(["pacman", "-Q", "sox"],stdout=subprocess.PIPE).communicate()[0]
'''

# Ask user where the music is stored
print ("\n\n\nHello, I will help you rename your music ^.^")
print ("Please enter the directory your music is in.")
print ("Enter it like: /home/username/music\n")
#musicDir = input("Directory:")
musicDir = "/home/mitch/Music/"

# Walk that directory and build array of files
files = []
#folders = []
for (path, dirnames, filenames) in os.walk(musicDir):
    #folders.extend(os.path.join(path, name) for name in dirnames)
    files.extend(os.path.join(path, name) for name in filenames)

# iterate through files array and use regex to replace " " with "\ " so we can navigate directories
for i in range (len(files)):
    tempString = str(files[i])
    files[i] = re.sub("\s", "\ ", tempString)

# play song until keyboard interupt
# should make this section a new color
for i in range(len(files)):
    os.system("play " + files[i])
    print ("\nKeyboard interupt detected\n")
    inputName = input("Name this file: ")
    # TODO: add error checking so name is valid
    inputName = musicDir + "/" inputName
    print (inputName)
#    os.rename(files[i], inputName)



