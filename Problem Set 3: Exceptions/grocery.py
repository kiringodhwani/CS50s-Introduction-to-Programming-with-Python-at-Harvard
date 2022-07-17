# Define a dictionary to store the user's grocery list
groceries = dict()

# Take in grocery items from the user until they input control-d
while True:
    try:
        s = input().upper()

        # If the user's input is already an item (key) in the grocery list, increment it's count (value) by 1
        if s in groceries:
            groceries[s] = groceries.get(s) + 1

        # Otherwise, we add the new grocery item as a key in the dict with a count (value) of 1
        else:
            groceries[s] = 1

    # Catch KeyErrors
    except KeyError:
        pass

    # Detect when the user inputs control-d
    except EOFError:

        # Sort the grocery list alphabetically
        groceries = dict(sorted(groceries.items()))

        # Print the grocery list and format by prefixing each item (key) by its count (value)
        for i in groceries:
            print(groceries[i], i)

        break

