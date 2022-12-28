import os
import subprocess

def download_clip(url, output_prefix):
    # Create the "cache" subfolder if it doesn't exist
    if not os.path.exists("cache"):
        os.makedirs("cache")

    # Use yt-dlp to download the clip
    subprocess.run(["yt-dlp", url, "-o", f"cache/{output_prefix}.mp4"])

    # Use ffmpeg to split the clip into individual frames
    subprocess.run(["ffmpeg", "-i", f"cache/{output_prefix}.mp4", "-vf", "fps=10/1", f"cache/{output_prefix}_%03d.png"])
   

def create_gif(input_prefix, start_frame, end_frame, output_filename, top, left, width, height):
    # Use ffmpeg to generate the GIF Area
    subprocess.run(["ffmpeg", "-i", f"cache/{output_prefix}_%03d.png", "-vf", f"crop=448:448:{left}:{top}", f"cache/cropped_{output_prefix}_%03d.png"])
    
    # Generate the palette using ffmpeg
    subprocess.run(["ffmpeg", "-y", "-f", "image2", "-start_number", str(start_frame), "-i", f"cache/cropped_{input_prefix}_%03d.png", "-vf", f"fps=10,scale={width}:{height}:flags=lanczos,palettegen=stats_mode=single", f"cache/palette_{input_prefix}_%03d.png"])

    # Create the GIF using ffmpeg
    subprocess.run(["ffmpeg", "-y", "-f", "image2", "-start_number", str(start_frame), "-i", f"cache/cropped_{input_prefix}_%03d.png", "-i", f"cache/palette_{input_prefix}_%03d.png", "-lavfi", f"fps=10,scale=112:112:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle", output_filename])

# Get the URL from the user
url = input("Enter the URL of the clip: ")
output_prefix = "clip"

# Download the clip
download_clip(url, output_prefix)

# Get the start and end frames from the user
start_frame = int(input("Enter the start frame: "))
end_frame = int(input("Enter the end frame: "))
output_filename = input("Enter the output filename: ")

# Get the top and left coordinates of the area from the user
top = int(input("Enter the top coordinate of the area: "))
left = int(input("Enter the left coordinate of the area: "))

# Set the width and height of the area to 448x448 pixels
width = 448
height = 448

# Create the GIF
create_gif(output_prefix, start_frame, end_frame, output_filename, top, left, width, height)
