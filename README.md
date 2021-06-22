
# mp3 + wav renamer

## Overview
I wrote this program to help me organize my music library.
Each mp3 or wav is read into a list. The list is iterated, playing each track until a keyboard interrupt (CTRL + C).  
The user is then asked to rename the track, delete it, or keep it.
The script will prevent invalid track names, invalid directories, and detect the correct file extensions (mp3 and wav).

## Dependencies
* This script uses the [colorama](https://github.com/tartley/colorama) module which is distributed under the BSD-3-Clause License.   
    * Install it with: `pip install colorama`
* This script uses [SoX](https://github.com/chirlu/sox) which is distributed under the GPL-2.0 License.
    * Debian based distros: `sudo apt install sox`  
    * Fedora: `sudo dnf install sox`

## Screenshot 
<img src="./screenshots/screen1.png" width="700" />
