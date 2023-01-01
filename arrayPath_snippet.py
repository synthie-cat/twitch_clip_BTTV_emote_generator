import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add the argument
parser.add_argument("--leftpath", "-lp", nargs=3, type=int, help="Generate path from three numbers seperated by spaces")

# Parse the argument
args = parser.parse_args()

# Get the argument as a list of integers
pathArray = args.leftpath

# Do something with the array of integers
frame = 100
halfFrame = frame // 2

if pathArray[1] >= pathArray[0]:
	frameStep1 = round((pathArray[1] - pathArray[0]) / halfFrame)
else:
	frameStep1 = round((pathArray[0] - pathArray[1]) / halfFrame)
if pathArray[2] >= pathArray[1]:
	frameStep2 = round((pathArray[1] - pathArray[2]) / halfFrame)
else:
	frameStep2 = round((pathArray[2] - pathArray[1]) / halfFrame)


print(frameStep1)
print(frameStep2)