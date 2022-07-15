def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    # Make sure that the plate length is at least 2 characters and at most 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Loop through the individual characters in the string
    for i in range(len(s)):
        # Make sure that the current character is a letter or number
        if s[i].isalpha() == False and s[i].isdigit() == False:
            return False

        # First and second characters must be letters
        if i == 0 and s[i].isalpha() == False:
            return False
        if i == 1 and s[i].isalpha() == False:
            return False

        # Enter this conditional when the first number is encountered
        if s[i].isdigit() == True:
            # The first number can't be a 0
            if int(s[i]) == 0:
                return False
            # Call the rest_digit function on the remainder of the string to make sure it consists of all numbers
            if rest_digit(i+1, s) == True:
                return True
            else:
	            return False

    # Plate is all letters
    return True

# Returns true if all of the characters past the given index in the given string are numbers.
def rest_digit(index, string):
    # Loop through the substring past the given index. If a non-number character is found, return false.
    for i in range(index, len(string)):
        if string[i].isdigit() == False:
            return False

    # No non-number characters found
    return True

main()
