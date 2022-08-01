import re


def main():
    print(convert(input("Hours: ")))

# Convert() expects a string (s) in one of the following 12-hour time formats: '9:00 AM to 5:00 PM' or '9 AM to 5 PM'
def convert(s):

    # The hour of any time in 12-hour format is between 1 and 12. This means that the first digit of the user-inputted hour is between 1 and 9, and
    # the second digit (which is optional) is between 0 and 2.
    # The program allows users to input a time without minutes. Thus, for each inputted time, the ':' and the number of minutes are optional.
    # Each time can be either AM or PM.
    # Capture the hour, number of minutes, and time of day (AM or PM) of both user-inputted times.
    if matches := re.search(r'^([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)$', s):
            
        # To ensure the times are formatted in 12-hour time, make sure that both times have an hour between 1 and 12, inclusive.
        if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
            raise ValueError

        # Convert both times to 24-hour format using the to_twenty_four() function.
        else:
            time1 = to_twenty_four(matches.group(1), matches.group(2), matches.group(3))
            time2 = to_twenty_four(matches.group(4), matches.group(5), matches.group(6))
            return f'{time1} to {time2}'

    else:
        raise ValueError

# Takes in the hour (as a string), number of minutes (as a string), and time of day (AM or PM) of a time in 12-hour format and 
# returns the same time as a string in 24-hour format.
def to_twenty_four(hour, minute, AMPM):

    # All times in PM, where the hour is not 12, must have 12 added to their hour to convert to 24-hour time.
    # If we are in PM and the hour is 12, we do nothing, because 12 P.M = 12:00 in 24-hour format.
    if AMPM == 'PM' and int(hour) != 12:
        hour = int(hour) + 12

    # 12 AM is equivalent to 0:00 in 24-hour time.
    if AMPM == 'AM' and int(hour) == 12:
        hour = 0

    # If the minute parameter has no value (i.e. the user originally chose to input a time without minutes), set the number of minutes to '00'.
    if not minute:
        minute = '00'

    # Return the time in 24-hour format, prefixing the hour with a 0 if it is a single digit.
    return f'{int(hour):02}' + ':' + minute

if __name__ == "__main__":
    main()
