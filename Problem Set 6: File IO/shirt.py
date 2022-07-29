import sys
import os
from PIL import Image, ImageOps

# Expects exactly two command-line arguments other than the filename.
# The first command-line argument after the filename is the name (or path) of a JPEG or PNG to read (i.e., open) as input.
# The second is the name (or path) of a JPEG or PNG to write (i.e., save) as output.
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    pass

# os.path.splitext splits the inputted path into a pair (root, ext). This allows us to isolate the file extensions.
input_split = os.path.splitext(sys.argv[1])
output_split = os.path.splitext(sys.argv[2])

# Make the extensions lowercase so that they can be treated case insensitively
input_ext = input_split[1].lower()
output_ext = output_split[1].lower()

# Make sure that both the input's extension and output's extension are one of '.jpg', '.jpeg', or '.png'.
# If either is not, exit the program.
if input_ext not in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid input')

if output_ext not in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid output')

# Make sure that the input file and output file have the same extension
if input_ext != output_ext:
    sys.exit('Input and output have different extensions')

# Open the input file (the first command-line argument after the filename). This file is an image.
try:
    input = Image.open(sys.argv[1])
# Catch FileNotFoundErrors raised by 'open' and exit with an error message
except FileNotFoundError:
    sys.exit('Input does not exist')

# Open the shirt file provided to us on the assignment ('shirt.png'). We know this file exists so no need to catch exceptions.
shirt = Image.open("shirt.png")

# Determine the size of the shirt file
size = shirt.size

# Resize and crop the input file to fit the shirt
input = ImageOps.fit(input, size)

# Overlay the shirt onto the input file / paste the shirt onto the input file.
# In the below tuple read into the paste function, the first shirt represents the image to overlay and the second shirt
# represents a “mask” indicating which pixels in photo to update.
input.paste(shirt, shirt)

# Save the image to the output file
input.save(sys.argv[2])
