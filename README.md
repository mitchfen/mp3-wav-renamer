
# mp3 + wav renamer

### Overview
I'm writing this program to help me organize my mess of a music library.
This program reads each mp3 or wav into a list, then iterates through them and plays each one until a keyboard interrupt (CTRL + C). The user is then asked to rename the song, delete it, or keep it.

The script will prevent invalid song names, invalid directories, and detect the right file extensions mp3 and wav.

### Screenshot

<img src="https://github.com/mitchfen/renameMyMusic/blob/master/screenshots/screen1.png" width="500" />

### Dependencies

**Colorama**
* `pip install colorama`

**SoX**
* `sudo apt-get install sox` on Debian and derivatives
* `sudo pacman -S sox` on Manjaro/Arch

### Running the program

Type `python main.py` into your shell.

### TODO

* Windows support:
    * SoX not workable on windows.
    * Have tried VLC without GUI but need a way to cancel playback
    * [cmdmp3](https://github.com/jimlawless/cmdmp3) could be workable
* Add functionality for moving songs into sub directories
* Add output to see progress
