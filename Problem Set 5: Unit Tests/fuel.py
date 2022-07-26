def main():
    # Take in user input
    s = input('Input a fraction: ')

    # Call convert to convert the user-inputted fraction to a % rounded to the nearest int
    n = convert(s)

    # Call gauge to determine the amount of fuel remaining based on the original fraction
    fuel = gauge(n)
    print(fuel)

# Converts the user-inputted fraction to a % rounded to the nearest int btw 0 and 100 inclus.
def convert(fraction):
    # Split the fraction at the slash
    vals = fraction.split('/', 1)

    # Make sure that the numerator and denominator are ints
    if not vals[0].isdigit() or not vals[1].isdigit():
        raise ValueError

    # Convert the numerator and denominator from strings to ints
    x = int(vals[0])
    y = int(vals[1])

    # The denominator of the fraction cannot be 0
    if y == 0:
        raise ZeroDivisionError

    # Make sure the numerator is not greater than the denominator because your gas
    # tank can't be more than 100% full
    if x > y:
        raise ValueError

    # Evaluate the fraction
    z = x / y

    # Multiple by 100 to convert to a percentage, then round to the nearest whole number and convert to an integer
    z = round(z * 100, 0)
    z = int(z)

    return z

# Expects an int and returns a str that is: "E" if that int is less than or equal to 1, "F" if that int is greater than or equal to 99, and "Z%" otherwise, wherein Z is that same int.
def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        # Convert the integer to a string in percentage format
        percentage = str(percentage)
        percentage = percentage + '%'
        return percentage

if __name__ == "__main__":
    main()
