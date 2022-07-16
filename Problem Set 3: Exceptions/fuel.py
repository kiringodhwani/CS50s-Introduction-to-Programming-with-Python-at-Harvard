# Take in input until the user inputs a valid fraction
while True:
    try:
        # Split the fraction at the slash
        vals = input('Input a fraction: ').split('/', 1)

        # Convert the numerator and denominator from strings to ints
        x = int(vals[0])
        y = int(vals[1])

        # Make sure the numerator is not greater than the denominator because your gas
        # tank can't be more than 100% full
        if x > y:
            continue

        z = x / y

    # Catch ValueError and ZeroDivisionError exceptions
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

# Multiple by 100 to convert to a percentage and then round to the nearest whole number
z = round(z * 100, 0)

# Convert to an integer to remove '.0' from the output
percentage = int(z)

# If 1% or less remains, we output E for an empty tank.
# If 99% or more remains, we output F for a full tank.
if percentage >= 99:
    print('F')
elif percentage <= 1:
    print('E')
else:
    # Convert the integer to a string in percentage format
    percentage = str(percentage)
    percentage = percentage + '%'
    print(percentage)
