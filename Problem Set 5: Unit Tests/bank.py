# Main Function
def main():
    g = input('Enter a greeting: ')

    # Call the value fxn to determine the value of the user-inputted greeting. Print said value.
    n = value(g)
    print(n)

# Determines the value of the greeting passed in
def value(greeting):
    # Make the greeting string lowercase so that it can be treated case-insensitively
    greeting = greeting.lower()

    # Return 0 if the string starts with “hello”, 20 if it starts with an “h” (but not “hello”), or 100
    if greeting.startswith('hello') == True:
        return 0
    elif greeting.startswith('h') and greeting.startswith('hello') == False:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
