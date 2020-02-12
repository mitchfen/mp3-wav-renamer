import os
import sys
from pathlib import Path
from platform import system
from re import search
from colorama import Fore, Style, deinit, init

init() # initialize colorama

def getMusicDirectory():
    # Ask user where the music is stored
    print (Fore.GREEN + "\nPlease enter the directory your music is in.")
    print ("Enter it like: /home/username/music")
    print ("or C:\\Users\\mitch\\Music\n")
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
            #os.system('cls')
            print("Sorry, windows development ongoing... Not working yet")
            deinit() # need to stop colorama before exiting 
            sys.exit()
        elif system() =='Linux':
            os.system('clear')
            os.system("play " + "\"" + files[i] + "\"")
        else:
                print("\nCannot determine OS, exiting...\n")
                deinit() # stop colorama before exiting
                sys.exit()
        # After keyboard interrupt:
        renamePrompt(i)

    deinit() #stop colorama

def renamePrompt(i):
    print(Style.RESET_ALL)
    print("Name this file(x to delete, k to keep) do not include extension.")
    unsanitizedName = input("Name: ")
    # pass the desired name to check it before continuing
    if unsanitizedName== "x":
        cmd = ("rm " + "\"" + files[i] + "\"")
        os.system(cmd)     
        print(Fore.RED + "Deleted.")
        print(Style.RESET_ALL)
    elif unsanitizedName== "k":
        print(Fore.RED + "Keeping file as " + files[i])
        print(Style.RESET_ALL)
    else:
            newName = sanitizeSongName(unsanitizedName)
            renameSong(files[i], newName)

def renameSong(pathToSong, newName):            
    # Add appropriate extension to the song
    if pathToSong[len(pathToSong)-1] =="3": # mp3 file
        newName = musicDir + newName +".mp3"
    elif pathToSong[len(pathToSong)-1] =="v": # wav file
        newName = musicDir + newName +".wav"
    # Detect if song with that name already present
    AlreadyExists = os.path.exists(newName)
    if (AlreadyExists):
        secondaryName = input("Name already in use, please rename: ")
        sanitizeSongName(secondaryName)
        renameSong(pathToSong, secondaryName)
    else:  
        # want to confirm rename in red
        print(Fore.RED + "Renaming to " + newName)  
        print(Style.RESET_ALL)
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