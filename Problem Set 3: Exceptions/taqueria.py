# Dictionary of offered entrees
entrees = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize a variable to 0.00 to be used to increment the user's total
price = 0

# Take in user orders until they input control-d
while True:

    try:
        # Take in user input and title case it since the keys in the dict are title cased
        s = input('Item: ').title()

        # If the user's order is not a key in the dict, then end the current iteration of the loop and re-prompt the user
        if s not in entrees:
            continue

        # Retrieve the price associated with the user's order
        order = entrees.get(s)

        # Increment the current price value by adding the current order
        price = price + order

        # Format the value to be printed: change to two decimal places, convert to a str, add a leading dollar sign
        to_print = '{:.2f}'.format(price)
        to_print = '$' + to_print
        print(to_print)

    # Detect Value Errors
    except ValueError:
        pass

    # Detect when the user inputs control-d
    except EOFError:
        print()
        break


