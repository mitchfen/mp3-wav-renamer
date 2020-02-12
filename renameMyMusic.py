import os
import sys
from pathlib import Path
from platform import system
from re import search
from colorama import Fore, Style, deinit, init

init() # initialize colorama

def getMusicDirectory():
    # Ask user where the music is stored
    print (Fore.GREEN + "\nHello, I will help you rename your music.")
    print ("Please enter the directory your music is in.")
    print ("Enter it like: /home/username/music\n")
    print(Style.RESET_ALL)
    print (Fore.BLUE + "Directory: ", end = "")   # want input on same line, different color
    print(Style.RESET_ALL, end = "")
    musicDir = input()
    # Ensure directory terminates in correct symbol.
    # Need a / on Unix, \ for Windows
    if system() == 'Windows':
        if musicDir[len(musicDir)-1] != "\"":
            musicDir += "/"
    if system() == 'Linux':
        if musicDir[len(musicDir)-1] != "/":
            musicDir += "/"
    # Ensure path is valid, we don't want to start running rm operations on a bad directory
    assert os.path.exists(musicDir), "ERROR "+str(musicDir) + " is an invalid directory"
    return musicDir

def collectSongs(musicDir, files = []):
    # Walk the directory and build list of files
    for (path, dirnames, filenames) in os.walk(musicDir):
        files.extend(os.path.join(path, name) for name in sorted(filenames))
    return files

def mainLoop(musicDir, files = []):
    for i in range(len(files)):
        # I want the sox output to be yellow so I can distinguish from my python
        print (Fore.YELLOW) 
        # need to wrap file names in quotes so they are read properly
        if system() == 'Windows':
            #os.system("vlc --intf dummy " + "\"" + files[i] + "\"")
            print("Sorry, windows development ongoing... Not working yet")
            deinit() # need to stop colorama before exiting 
            sys.exit()
        elif system() =='Linux':
            os.system("play " + "\"" + files[i] + "\"")
        else:
                print("\nCannot determine OS, exiting...\n")
                deinit() # stop colorama before exiting
                sys.exit()
        # After keyboard interrupt:
        actionOnFile(i)

    deinit() #stop colorama

def actionOnFile(i):
    print(Style.RESET_ALL)
    print("Name this file(x to delete, k to keep) do not include extension.")
    uncheckedName = input("Name: ")
    # pass the desired name to check it before continuing
    songName = sanitizeSongName(uncheckedName)

    if songName== "x":
        cmd = ("rm " + "\"" + files[i] + "\"")
        os.system(cmd)     
        print(Fore.RED + "Deleted.")
        print(Style.RESET_ALL)
    elif songName == "k":
        print(Fore.RED + "Keeping file as " + files[i])
        print(Style.RESET_ALL)
    else:
        if files[i][len(files[i])-1] == "3": # mp3 file
            songName = musicDir + songName + ".mp3"
            renameSong(files[i], songName)
        elif files[i][len(files[i])-1] == "v": # wav file
            songName = musicDir + songName + ".wav"
            renameSong(files[i], songName)
        else:
            print(Fore.RED + "Renaming to")

def renameSong(pathToSong, newName):            
    print(Fore.RED + "Renaming to " + newName)    # want to confirm rename in red
    print(Style.RESET_ALL)
    # mv bash command must recieve two arguments in quotes
    cmd = ("mv " + "\"" + pathToSong + "\"" + " " + "\"" + newName + "\"")
    os.system(cmd)

def sanitizeSongName(nameToCheck):
    # ensure that name the user wants does not contain weird characters
    # only spaces and alphanumerics are allowed
    # multiple spaces are allowed but seriously.. don't do that
    keepGoing = True
    while(keepGoing):
        validName = search("^[a-zA-Z0-9\s]+$", nameToCheck)
        if(validName):
            keepGoing = False
        else:
            print("Error this is not a valid name")
            nameToCheck = input("Please try again: ")
    return nameToCheck

musicDir = getMusicDirectory()
files = []
files = collectSongs(musicDir, files)
mainLoop(musicDir, files)