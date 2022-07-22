# Read in greeting
g = input('Enter a greeting: ')

# Strip leading whitespace and make lowercase so that we can treat the user's greeting case insensitively.
g = g.lstrip().lower()

# Print 0 if the string starts with “hello”, 20 if it starts with an “h” (but not “hello”), or 100
if g.startswith('hello') == True:
	print('$0')
elif g.startswith('h') and g.startswith('hello') == False:
	print('$20')
else:
	print('$100')
