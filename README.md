# twitch_clip_BTTV_emote_generator
 Python Script that uses FFMPEG to generate BTTV ready emotes

There's still some handywork required - mostly because this is a pretty useless, small script.

## How to use:
1. Download and install [Python](https://www.python.org/downloads/windows/); Linux users please use your package manager to do so; Mac Users stop using Mac.
1. Download and install [ffmpeg](https://ffmpeg.org/download.html)
1. Run `pip install -r requirements.txt` to install `yt-dlp`
1. Open a CLI (Windows: PowerShell) and run `python bttv_emote_maker.py`
1. Paste the URL of the Clip you want to use. You could technically also use complete VODs but that's going to generate a fuckton of garbo. Don't.
1. When promoted to `Enter the start frame:` navigate to the `Scrip Folder => cache`. Scroll through the images to select your start enter the number (e.g. You want to start with clip_038.png enter 038. Keep the leading 0)
1. When promted to `Enter the end frame:` do the same as above - just chose where your BTTV Emote should end
1. Enter the desired file name ending in .gif (e.g. `kiviSkills.gif`)
1. Open the Starting Frame in an image program. For ease of use I recommend something thats easily available such as [PhotoPea](https://photopea.com)
1. Use the selection tool and set it to a **fixed size** of 448×448px. Select the area you want to use and note the top coordinate and the left coordinate. (e.g. 557px from Top, 1382px from the left)
1. Wait until the script is done. It will now crop the picutre, generate a GIF palette and create a 112×112px GIF that can be used on BTTV.

## Disclaimer:
This is mostly a little BS thing I did and offer as is. Feel free to fork and improve, I am done with it. :) 