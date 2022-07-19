import random

# Take in input from the user until they input a positive integer
while True:
    try:
        n = int(input('Level: '))

        # Make sure that the input is a positive integer; otherwise, re-prompt
        if n < 1:
			      continue

    # Catch ValueErrors
    except ValueError:
        pass
 
    else:
		    break

# Randomly generate an int in the range [1,n]
rand = random.randint(1,n)

# While loop that ends when the user correctly guesses the number
while True:
    try:
        # Request a guess from the user
        guess = int(input('Guess: '))

        # Make sure user input is positive
        if guess < 0:
            continue

        # Guess is too small
        if guess < rand:
            print('Too small!')

	    # Guess is too large
        elif guess > rand:
            print('Too large!')

	    # Guess is correct
        else:
            print('Just right!')
            break

    # Catch ValueErrors in case the user inputs a non-int value
    except ValueError:
        pass




