# Read in input
camel_case = input('Enter the name of a variable in camel case: ')

# Set a variable equal to the first character in the input string. We know that this character will be
# lowercase since the input is in camel case. We will then use this variable to build the string in snake case
build = camel_case[0]

# Begin iterating through the remaining characters in the input string skipping the first character
for c in camel_case[1:]:

	# If the current character is an uppercase letter, then append an underscore to the building string 
	# followed by the current character in its lowercase form
	if c.isupper() == True:
		build = build + '_' + c.lower()
		
	# If the current character is lowercase, simply append it to the building string
	else:
		build = build + c.lower()

print(build)
