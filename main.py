import os
import sys
import platform
import re

# Attempt to import colorama if module installed
try:
    import colorama
except ImportError:
    print("You need to install the colorama module using \"pip install colorama\" before proceeding")
    sys.exit()

# Attempt to import winsound - need this on Windows but not for Linux
try:
    import winsound
except ImportError:
    pass

def collectSongs(musicDir, files = []):
   
    # Walk the directory and build list of files
    for (path, dirnames, filenames) in os.walk(musicDir):
        files.extend(os.path.join(path, name) for name in sorted(filenames))

    # Remove files which are not music
    # Will be faster to do an if statement inside the above loop
    i = 0
    while (i < len(files)-1):
        if not files[i].endswith('.mp3') and not files[i].endswith('wav'):
            files.pop(i)
        i = i + 1

    return files

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

def getMusicDirectory():

    # Ask user where the music is stored 
    # Color this section green
    print (colorama.Fore.GREEN + "\nPlease enter the directory your music is in.")
    print ("Linux ex: /home/yourUsername/music")
    print("Windows ex: C:\\Users\yourUsername\\music")
    print(colorama.Style.RESET_ALL)
    print (colorama.Fore.MAGENTA + "Directory: ", end = "")   # want input on same line, different color
    print(colorama.Style.RESET_ALL, end = "")
    musicDir = input()

    # Ensure directory terminates in correct symbol.
    # Need to terminate in \ on Windows
    if platform.system() == 'Windows':
        if musicDir[len(musicDir)-1] != "\\":
            musicDir += "\\"

    # Need a / on Unix
    if platform.system() == 'Linux':
        if musicDir[len(musicDir)-1] != "/":
            musicDir += "/"

    # Ensure path is valid, we don't want to start running rm operations on a bad directory
    assert os.path.exists(musicDir), "ERROR "+str(musicDir) + " is an invalid directory"
    return musicDir

def mainLoop(musicDir, files = []):

    # Loop throught the list, playing each file until keyboard interupt, then rename/keep/delete
    # Continue looping until each file in the list is handled then program terminates

    for i in range(len(files)):
        
        # I want the sox output to be yellow so I can distinguish from my python
        print (colorama.Fore.GREEN)
        
        if platform.system() == 'Windows':
            print(colorama.Style.RESET_ALL)
            print(colorama.Fore.GREEN + "\nPlaying:\n" + files[i] +"\n")
                      
            winsound.PlaySound(files[i], winsound.SND_ASYNC)

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
#checkIfwinsoundNeeded()
colorama.init() # per colorama documentation
musicDir = getMusicDirectory()
files = []
files = collectSongs(musicDir, files)
mainLoop(musicDir, files)