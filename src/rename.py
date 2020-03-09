import os
import sys
import platform
import colorama
import re 

def renamePrompt(i, files, passedDirectory):

    # Get user input for the name of the file, do this in color white
    print(colorama.Style.RESET_ALL)
    print("Name this file(x to delete, k to keep) do not include extension.")
    unsanitizedName = input("Name: ")

    if unsanitizedName== "x":
        cmd = ("rm " + "\"" + files[i] + "\"")
        os.system(cmd)     
        print(colorama.Fore.RED + "Deleted.")
        print(colorama.Style.RESET_ALL)
    elif unsanitizedName== "k":
        print(colorama.Fore.RED + "Keeping file as " + files[i])
        print(colorama.Style.RESET_ALL)
    # if the name is not k or x, it must be sanitized to remove invalid characters before renaming
    else:
        newName = sanitizeSongName(unsanitizedName)
        renameSong(files[i], newName, passedDirectory)

def renameSong(pathToSong, newName, passedDirectory):            

    if pathToSong.endswith('.mp3'):
        newName = passedDirectory + newName +".mp3"
    elif pathToSong.endswith('.wav'):
        newName = passedDirectory + newName +".wav"
    
    # Detect if file with same name already exists
    # NOTE: This intentionally allows both song.mp3 and song.wav to exist. 
    #               Such a scenario is not detected
    if os.path.exists(newName):
        secondaryName = input("Name already in use, please rename: ")
        sanitizeSongName(secondaryName)
        renameSong(pathToSong, secondaryName, passedDirectory)

    # If the song name is unique, then we print out its new name in red
    # Then use mv command to rename file
    else:  
        print(colorama.Fore.RED + "Renaming to " + newName)  
        print(colorama.Style.RESET_ALL)
        cmd = ("mv " + "\"" + pathToSong + "\"" + " " + "\"" + newName + "\"")
        os.system(cmd)

def sanitizeSongName(nameToCheck):

    # ensure that name the user wants does not contain invalid characters
    # only spaces and alphanumerics are allowed
    keepGoing = True
    while(keepGoing):
        validName = re.search("^[a-zA-Z0-9\s]+$", nameToCheck)
        if(validName):
            keepGoing = False
        else:
            print("Error this is not a valid name")
            nameToCheck = input("Please try again: ")
    return nameToCheck