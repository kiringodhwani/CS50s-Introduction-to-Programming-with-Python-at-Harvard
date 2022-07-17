# Months list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Take in user input until they input a date in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
while True:
    try:
        s = input('Date: ').strip()

        # If the date is formatted like 9/8/1636, split the string into month, date, and year at the slashes
        if s[0].isdigit() == True:
            m, d, yr = s.split('/', 2)

        # If the date is formatted like September 8, 1636, split once at the first ' ' and then at ', ' to isolate m, d, yr
        elif s[0].isalpha() == True:
            mstring, dyr = s.split(' ', 1)
            d, yr = dyr.split(', ', 1)

            # Because the month is inputted as a string in this case, need to change it to its corresponding int
            # First determine if they inputted a valid month (months list is title cased)
            if mstring.title() in months:

                # Iterate through the months list
                for i in range(len(months)):

                    # When the month is found, set the numerical month equal to the current index in the months list + 1
                    # because the months list is in chronological order
                    if mstring == months[i]:
                        m = i + 1

            # If the user-inputted month is not in the months list, then they need to be re-prompted
            else:
                continue
        # If the first character in the input is not a letter or number, then the user must be re-prompted
        else:
            continue

        # Convert to ints to allow for integer comparisons
        m = int(m)
        d = int(d)
        yr = int(yr)

        # Need to validate that the inputted month, date, and year are valid
        # Month must be between 1 and 12
        if m < 1 or m > 12:
            continue

        # "Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days."
        if d < 1 or d > 31:
            continue

        # All dates are 4 digits
        if yr < 1000 or yr > 9999:
            continue

    except ValueError:
        pass

    else:
        break

# Format to YYYY-MM-DD format and then print
# Month must be two digits and a string
if m < 10:
    m = f'{m:02}'
else:
    m = str(m)

# Day must be two digits and a string
if d < 10:
    d = f'{d:02}'
else:
    d = str(d)

date = str(yr) + '-' + m + '-' + d

print(date)

