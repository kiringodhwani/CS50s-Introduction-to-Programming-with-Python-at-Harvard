from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dob = input('Date of Birth: ')

    # Use the user_input() function to validate the user-inputted birthdate and convert it to a date object.
    birthdate = user_input(dob)

    # Use the find_difference() function to calculate the minute difference between the birthdate and today's date. find_difference() also
    # formats this minutes value into a string to be printed to the user.
    to_print = find_difference(birthdate)
    print(to_print)

# Takes in a date (in the form of a date object), calculates the difference in minutes between said date and today's date, and then formats said
# difference in minutes like the following: 12345 --> "one thousand, two hundred thirty-four minutes". Lastly, returns the formatted string.
def find_difference(birthdate):
    # Get today's date.
    today = date.today()

    # Calculate the difference between today's date and the birthdate.
    difference = today - birthdate

    # The difference is initially in days, so we must convert it to minutes.
    seconds = difference.days * 24 * 60

    # Use the inflect module to format the output (i.e. 12345 --> "one thousand, two hundred thirty-four") and also capitalize the output.
    to_print = p.number_to_words(seconds, andword="")
    to_print = to_print.capitalize()
    to_print = to_print + ' minutes'

    return to_print

# Determines if a date of birth is in YYYY-MM-DD format. Exits via sys.exit if the user does not input a date in YYYY-MM-DD format
# or if the inputted date has a year, month, or day that is invalid.
def user_input(dob):
    try:
        # Use a regular expressions to ensure the date is formatted like YYYY-MM-DD.
        if not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', dob):
            sys.exit('Invalid date')

        yr, m, d = dob.split('-', 2)
        yr = int(yr)
        m = int(m)
        d = int(d)

        # Create a date object.
        # Raises a ValueError if the year, month, or day arguments are invalid. (e.g. month is less than 1 or greater than 12).
        birthdate = date(yr, m, d)

    except ValueError:
        sys.exit('Invalid date')

    else:
        return birthdate

if __name__ == "__main__":
    main()
