import random

# Main function
def main():
    # Initialize a variable to 0 which will be used to keep track of the user's score
    score = 0

    # Use get_level() to get a level from the user
    lvl = get_level()

    # for loop with 10 iterations
    for _ in range(0, 10):
        # Generate a random integer x and a random integer y (both with "lvl" digits) using the generate_integer fxn.
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        # Build the equation to be displayed to the user
        eq = str(x) + ' + ' + str(y) + ' = '

        # Define a while loop with a maximum of three iterations
        j = 0
        while j < 3:
			      # Display equation to user and take in their integer answer
            answer = int(input(eq))

			      # If the user's answer to the equation is correct, increment their score by 1 and break the while loop
            # because the equation does not need to be re-displayed
            if answer == x+y:
                score += 1
                break
			      # If the user's answer is wrong, tell them, then increment the iteration count by 1. This is to ensure
            # that the while loop has no more than 3 iterations.
            else:
                print('EEE')
                j += 1

                # If j = 3, then the user has guessed incorrectly 3 times. They then have no more guesses left so we output the correct answer.
                if j == 3:
                    print(str(x) + ' + ' + str(y) + ' = ' + str(x+y))


    # Print the user's final score after they answer all 10 equations
    print('Score:', score)

# Prompts (and, if need be, re-prompts) the user for a level (either 1,2, or 3). Then, returns the level.
def get_level():

    # Take in input from the user until they input a valid level
    while True:
        try:
            level = int(input('Level: '))

            # Make sure that the inputted level is 1,2, or 3
            if level not in [1, 2, 3]:
                continue

        # Catch ValueErrors (i.e. user inputs a non-number)
        except ValueError:
            pass
        # If user inputs a valid level between 1 and 3, then return it.
        else:
            return level

# Returns a randomly generated non-negative integer with "level" digits
def generate_integer(level):

    #raises a ValueError if level is not 1, 2, or 3
    if level not in [1, 2, 3]:
        raise ValueError

    # Set the lower bound of a non-negative, "level"-digit number
    if level == 1:
        # If we are outputting equations with single digit numbers, 0 must be the lower bound
        range_start = 0
    else:
        # With 2-digit numbers, the lower bound is 10. With 3-digit numbers, it is 100.
        range_start = 10**(level-1)

    # Set the upper bound of a non-negative, "level"-digit number. These are 9, 99, and 999.
    range_end = (10**level)-1

    # Use the bounds to generate a non-negative integer with "level" digits
    rand = random.randint(range_start, range_end)

    return rand

if __name__ == "__main__":
    main()

