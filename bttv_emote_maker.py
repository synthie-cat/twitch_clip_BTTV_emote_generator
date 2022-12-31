import os
import subprocess
import shutil

# Create the cache folder if it doesn't exist
shutil.rmtree("cache", ignore_errors=True)
os.makedirs("cache")

# Get the URL of the video from the user
url = input("Enter the URL of the clip: ")

# Download the video using yt-dlp
subprocess.run(["yt-dlp","-q","--progress", "-o", "cache/video.mp4", url])

print("Slicing clip into PNGs")

# Split the video into frames with a frame rate of 10 fps
subprocess.run(["ffmpeg", "-loglevel", "quiet", "-i", "cache/video.mp4", "-vf", "fps=10/1", "cache/clip_%03d.png"])

print("Open Cache folder to pick frames")

# Get the start and end frames from the user
start_frame = int(input("Enter the start frame: "))
end_frame = int(input("Enter the end frame: "))
filename = input("Enter the emote filename: ") or "new_bttv_emote.gif"

# Get the desired width, height, x, and y coordinates from the user
x = int(input("Enter the top coordinate: "))
y = int(input("Enter the left coordinate: "))
width = int(input("Enter area width (default: 448): "))
height = int(input("Enter area height (default: 448): "))

print("Generating emote...")

index = 0

# Crop the frames using ffmpeg
for i in range(start_frame, end_frame+1):
    subprocess.run(["ffmpeg","-loglevel", "quiet", "-i", f"cache/clip_{i:03d}.png", "-filter:v", f"crop={width}:{height}:{x}:  {y}", "-frames:v", "1", f"cache/cropped_{index:03d}.png"])
    subprocess.run(["ffmpeg", "-loglevel", "quiet", "-y", "-i", f"cache/cropped_{index:03d}.png", "-vf", "palettegen=stats_mode=single", f"cache/palette_{index:03d}.png"])
    index += 1

subprocess.run(["ffmpeg", "-loglevel", "quiet", "-i", f"cache/cropped_%03d.png", "-i", f"cache/palette_%03d.png", "-lavfi", "fps=10,scale=112:112:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle", filename])

print(f"Emote {filename} successfully generated.")
