import sys
import os

# Count variable to keep track of the number of lines of code
count = 0

# Program expects exactly one command-line argument other than the filename
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    pass

# This additional command-line argument is meant to be a python file.
# Isolate the extension of said argument and make sure that it is '.py'
root_ext = os.path.splitext(sys.argv[1])
extension = root_ext[1]
if extension != '.py':
    sys.exit('Not a python file')

try:
    with open(sys.argv[1]) as file:
	# For each line in the file...
        for line in file:
            # ...strip the leading whitespace…
            line = line.lstrip()

            #...check if the line starts with a '#'. If so, it is a comment, not a line of code.
            if line.startswith('#'):
                continue

            # …check if the line contains only whitespace characters or is empty. If either is true, it is not a line of code.
            if line.isspace() or line == '':
                continue

            # Since the current line of code is not a comment, is not only whitespace, and is not empty, we can consider it a line of code.
            count += 1

# Catch FileNotFoundErrors raised by 'open' and exit with an error message
except FileNotFoundError:
    sys.exit('File does not exist')

print(count)
