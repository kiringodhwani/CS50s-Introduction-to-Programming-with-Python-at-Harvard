# Read in expression
expression = input('Enter expression: ')

# Split the expression at the spaces to isolate each part of the expression
x, y, z = expression.split(' ', 2)

# Convert the numbers in the expression to integers
x = float(x)
z = float(z)

# If statement to determine the operation that is performed
if y == '+':
	print(x+z)
elif y == '-':
	print(x-z)
elif y == '*':
	print(x*z)
else:
	print(x/z)
