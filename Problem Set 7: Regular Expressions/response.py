from validator_collection import validators, checkers, errors

to_validate = input('What\'s your email address? ')

try:
    # Use the built-in email() function from validator-collection.
    # If the email is valid, sets the variable called 'validation' equal to said email. If the email is invalid, raises a ValueError.
    validation = validators.email(to_validate)

	  # If the email() function does not raise an error, then the email is valid
	  print('Valid')

# If the email() function raises an error, then the email is invalid
except (errors.EmptyValueError, errors.InvalidEmailError, ValueError):
	  print('Invalid')
