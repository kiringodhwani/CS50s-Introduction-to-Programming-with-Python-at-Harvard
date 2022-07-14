# Read in filename
filename = input('Enter the name of a file: ')

# Make lowercase so we can treat file extensions case insensitively
filename = filename.lower().strip()

# if statement
if filename.endswith('.gif') == True:
	print('image/gif')
elif filename.endswith(('.jpg', '.jpeg')) == True:
	print('image/jpeg')
elif filename.endswith('.png') == True:
	print('image/png')
elif filename.endswith('.pdf') == True:
	print('application/pdf')
elif filename.endswith('.txt') == True:
	print('text/plain')
elif filename.endswith('.zip') == True:
	print('application/zip')
else:
	print('application/octet-stream')

