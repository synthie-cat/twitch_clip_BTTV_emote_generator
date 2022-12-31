# BTTV Emote Maker
Platform agnostic command line script that generates BTTV emotes from video sources.

## Prerequisites

To run this script, you will need to have the following software and libraries installed on your system:

- Python 3.6 or higher
- ffmpeg
- yt-dlp (can be installed via `pip install -r requirements.txt`)

Make sure that you have the latest versions of these tools installed on your system before running the script.

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

| Argument | Short form | Description |
| --- | --- | --- |
| `--regen` | `-rg` | Regenerate emote based on previous download. |
| `--followleft` | `-fl` | Make left coordinate cropping follow a linear distance in pixels per frame. |
| `--followtop` | `-ft` | Make top coordinate cropping follow a linear distance in pixels per frame. |
| `--dir` | `-d` | Specify custom path. |
| `--fps` | `-f` | Slice with custom FPS. |
| `--outputsize` | `-os` | Change square output size. |
| `--verbose` | `-v` | Don't clear the shell. |
