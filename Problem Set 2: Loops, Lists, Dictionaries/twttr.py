# Take in user input
input = input('Input a string of text: ')

# Define an empty string to be used to build the abbreviated version of the input
abbrev = ''

# Loop through the individual characters in the string
for i in range(len(input)):

	# If the current character is not a vowel, append it to the abbreviated string
	if input[i] not in {'A','E','I','O','U','a','e','i','o','u'}:
		abbrev = abbrev + input[i]

# When the for loop finishes, the abbreviated string will be built
print(abbrev)
