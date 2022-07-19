import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

# Expects zero or two command-line arguments (not including the filename)
if len(sys.argv) != 1 and len(sys.argv) != 3:
	sys.exit('Invalid usage')

# Zero command line arguments other than the filename if the user would like to output text in a random font
if len(sys.argv) == 1:

    # Take in user input
    s = input('Input: ')

    # Choose a random font from the list of fonts
    f = random.choice(figlet.getFonts())

    # Set the font and output the text in said font
    figlet.setFont(font = f)
    print('Output: ')
    print(figlet.renderText(s))

# Two command line arguments other than the filename if the user would like to use a specific font
else:
    # The 1st argument after the filename should be either -f or -font and the 2nd should be a font
    minus = sys.argv[1]
    f = sys.argv[2]

    # Make sure the 1st argument other than the filename is either -f or -font
    if minus not in ['-f', '-font']:
        sys.exit('Invalid usage')

    # Make sure that the 2nd argument other than the filename is a valid font
    if f not in figlet.getFonts():
        sys.exit('Invalid usage')

    # Since we now know the arguments are valid, we take in the text the user would like to print
    s = input('Input: ')

    # Set the font and output the text in said font
    figlet.setFont(font = f)
    print('Output: ')
    print(figlet.renderText(s))

