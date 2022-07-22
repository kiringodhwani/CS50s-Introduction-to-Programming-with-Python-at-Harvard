# Read in greeting
g = input('Enter a greeting: ')

# Strip leading whitespace and make lowercase so that we can treat the user's greeting case insensitively.
g = g.lstrip().lower()

# if statement
if g.startswith('hello') == True:
	print('$0')
# Make sure that it doesn't start with 'Hello'
elif g.startswith('h') and g.startswith('hello') == False:
	print('$20')
else:
	print('$100')
