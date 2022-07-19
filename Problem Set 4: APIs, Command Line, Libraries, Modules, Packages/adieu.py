import inflect
p = inflect.engine()

# Initialize an empty list to be used to hold the user-inputted names
names = []

# Read in input (names) from the user until they input control-d
while True:
	try:
		s = input('Name: ')
		names.append(s)

	except EOFError:
		print()
		break

# Turn the list of names into a string list (i.e. ['Fred', 'Liesl', 'James'] --> 'Fred, Liesl, and James')
s = p.join(names)

# Format and print the result with 'Adieu, adieu, to '
to_print = 'Adieu, adieu, to ' + s
print(to_print)
