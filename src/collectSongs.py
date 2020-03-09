import os

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