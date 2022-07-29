import sys
import csv

# Expects exactly two command-line arguments other than the filename
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    pass

# Initialize an empty list
first_last_house = []

try:
	# The first additional command line argument is expected to be a CSV file whose columns are assumed to be 'name' and 'house' in order
	# Read the CSV file
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)

        # For each row in the CSV...
        for row in reader:
			      # Split the name column at ', ' to separate first and last name and remove the leading space in front of the first name
            # 'Godhwani, Kirin' —> 'Godhwani' and 'Kirin'
            first_last = row["name"].split(', ', 1)
            first = first_last[1]
            last = first_last[0]

			# Create a new dictionary with the fields: "first" (firstname), "last" (lastname), and "house".
            first_last_house.append({"first": first, "last": last, "house": row["house"]})

# Catch FileNotFoundErrors raised by 'open' and exit with an error message
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')


# Next, we write to a new CSV. We name this CSV the second additional command line argument passed in by the user.
with open(sys.argv[2], 'w') as file2:
    # Specify the column names of the new CSV to be "first" (firstname), "last" (lastname), and "house"
    writer = csv.DictWriter(file2, fieldnames = ["first", "last", "house"])

	  # The first row in the CSV is different from the others as it contains the header (column names):  "first", "last", "house
	  writer.writerow({"first": "first", "last": "last", "house": "house"})

	  # Add in the data from the individual dicts stored in the first_last_house list of dicts, organizing the values into the correct columns in the new CSV
	  for d in first_last_house:
		    writer.writerow({"first": d["first"], "last": d["last"], "house": d["house"]})

