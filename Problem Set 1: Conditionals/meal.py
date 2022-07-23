# Main function
def main():
    # Read in input
    t = input('Enter a time in 24-hour time format: ')

    t.lower().strip()

    # If the input is in 12-hour time format, call the TwelveHour fxn to convert the value to a float representing the
    # corresponding number of hours in 24-hour time.
    if t.endswith(('a.m.','p.m.')):
        t = TwelveHour(t)
    # If the input is already in 24-hour time, simply convert to a float representing the corresponding number of hours.
    else:
        t = convert(t)

    # If statement to determine what meal it is
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')
    else:
	# Do nothing
        pass

# Converts time, a string in 12-hour format, to the corresponding number of hours as a float (in 24-hour time).
def TwelveHour(time):
    time, ampm = time.split(' ', 1)

    # Replace the colon in the time format with a period and convert to a float
    time = time.replace(':', '.')
    time = float(time)

    # Add 12 hours to the time if it is in p.m.
    if ampm == 'a.m.':
        pass
    else:
        time = time + 12

    return time

# Converts time, a str in 24-hour format, to the corresponding number of hours as a float.
def convert(time):
    # Replace the colon in the time format to a period
    time = time.replace(':', '.')

    # Convert the string to a float
    time = float(time)

    return time


if __name__ == "__main__":
    main()
