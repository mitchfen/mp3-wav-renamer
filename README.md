# renameMyMusic.py

I am writing this python script to help me organize my mess of a music library.  This program reads each mp3 or wav into a list, then iterates through them and plays each one until a keyboard interrupt (CTRL + C). The user is then asked to rename the song, delete it, or keep it.

The script will prevent invalid song names, invalid directories, and detect the right file extensions mp3 and wav.

## Dependencies

Colorama:  `pip install colorama`  
SoX: Debian and derivatives: `sudo apt-get install sox` or `sudo pacman -S sox` on Manjaro  

## TODO

* Windows support: SoX not workable on windows.
    * Have tried VLC without GUI but need way to cancel playback
* Add functionality to move to sub directories
* Add output to see progress

## Screenshot

![broken-link](https://github.com/mitchfen/renameMyMusic/blob/master/screenshots/screen1.png)

