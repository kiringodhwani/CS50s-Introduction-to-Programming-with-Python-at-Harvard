# Main Function
def main():
    # Take in user input, call the shorten fxn to remove vowels from the input
    s = input('Input a string of text: ')
    abbrev = shorten(s)

    print(abbrev)

# Removes the vowels from the string passed in
def shorten(word):

    # Define an empty string we can use to build the string with no vowels
    build = ''
    # Loop through the individual characters in the string
    for i in range(len(word)):

        # If the current character is not a vowel, append it to the abbreviated string
        if word[i] not in {'A','E','I','O','U','a','e','i','o','u'}:
            build = build + word[i]

    # Return the resulting string with no vowels
    return build

if __name__ == "__main__":
    main()
