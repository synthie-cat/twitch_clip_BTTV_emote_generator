import os
import shutil
import subprocess
import argparse
import sys

def download_clip(url):
    # Download the video using yt-dlp
    print("Downloading the clip...")
    subprocess.run(["yt-dlp","-q","--progress", "-o", f"{dir_path}/video.mp4", url])
    split_video(fps)

def split_video(fps):
    # Split the video into frames
    print("Slicing clip into PNGs")
    subprocess.run(["ffmpeg", "-loglevel", "quiet", "-i", f"{dir_path}/video.mp4", "-vf", f"fps={fps}/1", f"{dir_path}/clip_%03d.png"])

    print(f"Open {dir_path} folder to pick frames")
    user_input()

def create_emote(start_frame, end_frame, filename, left, top, width, height, followLeft, followTop, size):
    print("Cropping and generating palettes...")
    index = 0

    # Crop the frames using ffmpeg
    for i in range(start_frame, end_frame+1):
        subprocess.run(["ffmpeg","-loglevel", "quiet", "-i", f"{dir_path}/clip_{i:03d}.png", "-filter:v", f"crop={width}:{height}:{left}:{top}", "-frames:v", "1", f"{dir_path}/cropped_{index:03d}.png"])
        subprocess.run(["ffmpeg", "-loglevel", "quiet", "-y", "-i", f"{dir_path}/cropped_{index:03d}.png", "-vf", "palettegen=stats_mode=single", f"{dir_path}/palette_{index:03d}.png"])
        index += 1
        left += followLeft
        top += followTop

    # Generate the GIF by stitching everything together using the palette as index
    print("Generating GIF...")
    subprocess.run(["ffmpeg", "-loglevel", "fatal", "-i", f"{dir_path}/cropped_%03d.png", "-i", f"{dir_path}/palette_%03d.png", "-lavfi", f"fps=10,scale={size}:{size}:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle", filename])

    file_size = os.stat(filename).st_size
    if file_size > 1048576:
        print("The generated emote is over 1MB and will be to big for BTTV. Reduce the amout of frames.")
        print(f"{filename} was generated")
    else:
        print(f"Emote {filename} successfully generated.")

def complete_run():
    # Get the URL of the video from the user
    url = input("Enter the URL of the clip: ")

    download_clip(url)

def user_input():# Get the specifications from user
    start_frame = input("Enter the start frame: ") or 000
    end_frame = input("Enter the end frame: ") or 100
    filename = input("Enter the emote filename: ") or "new_bttv_emote.gif"
    left = input("Enter the left coordinate: ") or 0
    top = input("Enter the top coordinate: ") or 0
    width = input("Enter area width (default: 448): ") or 448
    height = input("Enter area height (default: 448): ") or 448

    # Adding default values just in case
    start_frame = int(start_frame)
    end_frame = int(end_frame)
    left = int(left)
    top = int(top)
    width = int(width)
    height = int(height)

    create_emote(start_frame, end_frame, filename, left, top, width, height, followLeft, followTop, size)

# Check if ffmpeg is installed.
result = subprocess.run(["ffmpeg", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print("ffmpeg is not installed. The script won't run.")
    sys.exit()
else:
    pass

# Generate arguments and help.
parser = argparse.ArgumentParser()
# Add the arguments with shortened descriptions
parser.add_argument("--regen", "-rg", action="store_true", help="Regenerate emote from previous download.")
parser.add_argument("--followleft", "-fl", type=int, help="Make left coord. follow linear distance (px/frame).")
parser.add_argument("--followtop", "-ft", type=int, help="Make top coord. follow linear distance (px/frame).")
parser.add_argument("--dir", "-d", type=str, help="Specify custom path for output files.")
parser.add_argument("--fps", "-f", type=int, help="Slice with custom FPS (default: 10FPS).")
parser.add_argument("--outputsize", "-os", type=int, help="Change square output size (default: 112x112px).")
parser.add_argument("--verbose", "-v", action="store_true", help="Don't clear the shell when running the script.")
parser.add_argument("--localvideo", "-lv", type=str, help="Copy a local mp4 file to the specified directory.")

args = parser.parse_args()

# Argument Check: Cropping Path
if args.followleft is not None:
    followLeft = args.followleft
else:
    followLeft = 0

if args.followtop is not None:
    followTop = args.followleft
else:
    followTop = 0
# Argument Check: Custom Path
dir_path = args.dir or "cache"

# Argument Check: Change FPS
if args.fps is not None:
    fps = args.fps
else:
    fps = 10

# Argument Check: Local video copy
if args.localvideo:
    shutil.copy(args.localvideo, f"{dir_path}/video.mp4")
    split_video(fps)

# Argument Check: Change Output Size
if args.outputsize is not None:
    size = args.outputsize
else:
    size = 112

# Argument Check: Verbose
if args.verbose:
    pass
else:
    os.system("clear" if os.name == "posix" else "cls")

# Argument Check: Make GIF using the previous clip
if args.regen:
    # Clean Up
    for filename in os.listdir(dir_path):
        # Check if the file name matches either of the specified formats
        if filename.startswith("cropped_") and filename.endswith(".png") or filename.startswith("palette_") and filename.endswith(".png"):
            os.remove(os.path.join(dir_path, filename))
    user_input()
else:
    # Clean Up
    if os.path.exists(dir_path):
    # Delete the contents of the directory
        for filename in os.listdir(dir_path):
            os.remove(os.path.join(dir_path, filename))
    else:
        os.mkdir(dir_path)
    complete_run()
