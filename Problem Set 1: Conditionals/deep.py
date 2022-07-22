# Read in answer
n = input('What is the answer to the great question of life? ')

# Remove whitespace
n = n.strip()

# Check if equals 42 or if the lowercase version equals forty-two / forty two. We make it lowercase because we treat the user's answer case insensitively.
if n == '42' or n.lower() in {'forty-two', 'forty two'}:
	print('Yes')
else:
	print('No')
