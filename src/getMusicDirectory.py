import os
import platform
import colorama

def getMusicDirectory():

    # Ask user where the music is stored 
    # Color this section green
    print (colorama.Fore.GREEN + "\nPlease enter the directory your music is in.")
    print ("Linux ex: /home/yourUsername/music")
    print("Windows ex: C:\\Users\yourUsername\\music")
    print(colorama.Style.RESET_ALL)
    print (colorama.Fore.BLUE + "Directory: ", end = "")   # want input on same line, different color
    print(colorama.Style.RESET_ALL, end = "")
    musicDir = input()

    # Ensure directory terminates in correct symbol.
    # Need to terminate in / on Windows
    if platform.system() == 'Windows':
        if musicDir[len(musicDir)-1] != "\"":
            musicDir += "/"

    # Need a / on Unix
    if platform.system() == 'Linux':
        if musicDir[len(musicDir)-1] != "/":
            musicDir += "/"

    # Ensure path is valid, we don't want to start running rm operations on a bad directory
    assert os.path.exists(musicDir), "ERROR "+str(musicDir) + " is an invalid directory"
    return musicDir
