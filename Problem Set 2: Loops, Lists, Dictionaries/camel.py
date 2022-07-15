camel_case = input('Enter the name of a variable in camel case: ')

# Define a variable that is initially just equal to the first charin the input string. We know that 
# this character will be lowercase. We will use said string to build up the string in snake case.
build = camel_case[0]

# Begin iterating through the remaining characters in the input string skipping the first character
for c in camel_case[1:]:

# If the current character is in uppercase letter, then append an underscore to the building string 
# followed by the current character in its lowercase form
  if c.isupper() == True:
    build = build + '_' + c.lower()

	# If the current character is lowercase, simply append it to the building string
	else:
		build = build + c.lower()

print(build)
