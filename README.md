# BTTV Emote Maker
Platform agnostic command line script that generates BTTV emotes from video sources.

## Prerequisites

To run this script, you will need to have the following software and libraries installed on your system:

- Python 3.6 or higher
- ffmpeg 
- yt-dlp (can be installed via `pip install -r requirements.txt`)

Make sure that you have the latest versions of these tools installed on your system before running the script.

### Installing prerequesits for Linux:

Debian / Ubuntu: 
```bash
sudo apt-get update
sudo apt-get install python3 ffmpeg
pip3 install -r requirements.txt
```
	
Arch/Artix/Manjaro:
```bash
sudo payman -Sy
sudo pacman -S python ffmpeg
pip3 install -r requirements.txt
```

### Installing prerequesits for Windows:
- [Python Download](https://www.python.org/downloads/windows/)
- [ffmpeg Download](https://ffmpeg.org/download.html)

After installing python run:
```bash
pip3 install -r requirements.txt
```

### Installing prerequesits on Mac:
Using Homebrew:
```
brew install python3
brew install ffmpeg
pip3 install -r requirements.txt
```
## Useage

### Running the script

To run the `bttv_emote_maker.py` script, follow these steps:

1. Open a terminal or command prompt window.
1. Navigate to the directory where the script is located.
1. Run the script using the `python` command, followed by the script name:
   ```bash
   python bttv_emote_maker.py
   ```
1. When prompted, paste the URL of the Twitch clip you want to download.
1. The script will ask you to review the frames. To do that browse with your filebrowser to the script path and review the frames.
1. Set the start and end frames by entering the frame numbers when prompted.
1. Enter a filename for the emote.
1. Manually review which part of the images should be used for the GIF e.g. using [Photopea](https://photopea.com)
1. Enter the crop values for the top and left coordinates, as well as the width and height of the emote.

### Arguments

| Argument | Short Flag | Description |
|----------|------------|-------------|
| `--regen` | `-rg` | Regenerate emote from previous download. |
| `--followleft` | `-fl` | Make left coord. follow linear distance (px/frame). |
| `--followtop` | `-ft` | Make top coord. follow linear distance (px/frame). |
| `--dir` | `-d` | Specify custom path for output files. |
| `--fps` | `-f` | Slice with custom FPS (default: 10FPS). |
| `--outputsize` | `-os` | Change square output size (default: 112x112px). |
| `--verbose` | `-v` | Don't clear the shell when running the script. |
| `--localvideo` | `-lv` | Copy a local mp4 file to the specified directory instead of downloading. |

## Video Tutorial
[![Youtube Link to a Video Tutorial](https://youtu.be/SIOuQ6H-oDM)](https://youtu.be/SIOuQ6H-oDM)

## ToDo:
- Add none linear paths
- ~Add ability to use local videos~
