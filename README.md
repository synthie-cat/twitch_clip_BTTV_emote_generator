# Generate BTTV Emotes from Twitch Clips

This is a Python script that uses FFMPEG to generate BTTV ready emotes. It requires some manual steps to use, as it is a small and specific script.

## How to use:

1. Download and install [Python](https://www.python.org/downloads/windows/) on your system. If you are using Linux, please use your package manager to install it. If you are using a Mac, it is recommended to sell your Mac and switch to a different system. ;)
1. Download and install [ffmpeg](https://ffmpeg.org/download.html)
1. Use the green `Code` button on this site to download a ZIP File containing the script. 
1. Run `pip install -r requirements.txt` to install dependencies.
1. Open a command line interface (Windows users: PowerShell) and run `python bttv_emote_maker.py`
1. Paste the URL of the clip you want to use. You can technically also use complete VODs, but this will generate a large number of unnecessary files. It is not recommended to do so.
1. When prompted to `Enter the start frame:`, navigate to the `Script Folder => cache` and scroll through the images to select your start frame. Enter the number of the frame (e.g. If you want to start with `clip_038.png`, enter `038`. Make sure to keep the leading zero).
1. When prompted to `Enter the end frame:`, do the same as above - select the frame where you want your BTTV emote to end.
1. Enter the desired file name ending in `.gif` (e.g. `kiviSkills.gif`)
1. Open the starting frame in an image editing program. It is recommended to use a program that is easily available, such as [PhotoPea](https://photopea.com).
1. Use the selection tool and set it to a size that is a multiple of 112×112px for best results (default is: 448×448px). Select the area you want to use and note the top coordinate and the left coordinate. (e.g. 557px from top, 1382px from the left)
1. When prompted, use the size that you've chosen in the previous step.
1. Wait until the script is finished. It will now crop the picture, generate a GIF palette, and create a 112×112px GIF that can be used on BTTV. (Depending on the filesize it might not work on BTTV. Use fewer frames if that happens.)

Disclaimer:

This is a small script that I created for personal use and am sharing as-is. Feel free to fork and improve it. I am no longer working on it. :)