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

def rename(pathToSong, newName):            
    print(Fore.RED + "Renaming to " + newName)    # want to confirm rename in red
    print(Style.RESET_ALL)
    # mv bash command must recieve two arguments in quotes
    cmd = ("mv " + "\"" + pathToSong + "\"" + " " + "\"" + newName + "\"")
    os.system(cmd)

def getMusicDirectory():
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
    return musicDir

def getAndCheckSongName(nameToCheck):
    # ensure that name the user wants does not contain weird characters
    # only spaces and alphanumerics are allowed
    # multiple spaces are allowed but seriously.. don't do that
    keepGoing = True
    while(keepGoing):
        y = re.search("^[a-zA-Z0-9\s]+$", nameToCheck)
        if(y):
            keepGoing = False
        else:
            print("Error this is not a valid name")
            nameToCheck = input("Please try again: ")
    return nameToCheck

def playAndTakeInput(files = []):
    for i in range(len(files)):
        print (Fore.YELLOW) # I want the sox output to be yellow so I can distinguish from my python
        os.system("play " + "\"" + files[i] + "\"")
        print(Style.RESET_ALL)
        print("Name this file(x to delete, k to keep) do not include extension.")
        uncheckedName = input("Name: ")
        songName = getAndCheckSongName(uncheckedName)
        if songName== "x":
                cmd = ("rm " + files[i])
                os.system(cmd)      # this is always successful, albiet with risky rm command
                print(Fore.RED + "Deleted.")
                print(Style.RESET_ALL)
        elif songName == "k":
                print(Fore.RED + "Keeping file as " + files[i])
                print(Style.RESET_ALL)
        else:
            if files[i][len(files[i])-1] == "3": # mp3 file
                songName = musicDir + songName + ".mp3"
                rename(files[i], songName)
            elif files[i][len(files[i])-1] == "v": # wav file
                songName = musicDir + songName + ".wav"
                rename(files[i], songName)
            else:
                print(Fore.RED + "Renaming to") 
            
def collectSongs(musicDir, files = []):
    # Walk the directory and build array of files
    # Then iterate through files array and use regex to replace " " with "\ " so we can navigate directories
    # Example: /home/mitch/music/song\ with\ spaces.mp3
    for (path, dirnames, filenames) in os.walk(musicDir):
        files.extend(os.path.join(path, name) for name in sorted(filenames))
    for i in range (len(files)):
        tempString = str(files[i])
        files[i] = re.sub("\s", "\ ", tempString)
    return files

musicDir = getMusicDirectory()
files = []
collectSongs(musicDir, files)
playAndTakeInput(files)