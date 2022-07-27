import sys
import os
import csv
from tabulate import tabulate

# Expects exactly one command line argument other than the filename
# This additional command line argument is the name (or path) of a CSV file
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    pass

# Make sure that the additional command line argument is a CSV file (i.e. extension == '.csv')
root_ext = os.path.splitext(sys.argv[1])
extension = root_ext[1]
if extension != '.csv':
    sys.exit('Not a CSV file')

# Initialize an empty list to be used to store the values read in from the CSV
menu = []

try:
    # Open and read the CSV file
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)

		    # The CSV file has three columns: a type ('cheese') and then its corresponding prices in small and large
        for type, small, large in reader:

			      # Add the values from the CSV to a list, then append the new list to the menu list
            menu.append([type, small, large])

# Catch FileNotFoundErrors raised by 'open' and exit with an error message
except FileNotFoundError:
    sys.exit('File does not exist')

# Use tabulate to convert menu (a list of lists) into a table, formatted as ASCII art
# Set the first element in the menu list (the first row of data) as the header and choose 'grid' as the table format
print(tabulate(menu, headers = 'firstrow', tablefmt = 'grid'))

