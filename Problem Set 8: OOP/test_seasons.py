from seasons import find_difference, user_input
import pytest
from datetime import date

# Test the user_input function, which validates the user-inputted birthdate.
def test_user_input():
    # Test user_input() on input that is not formatted in YYYY-MM-DD format.
    with pytest.raises(SystemExit):
        user_input('February 5, 2002')
    with pytest.raises(SystemExit):
        user_input('I am hungry')
    with pytest.raises(SystemExit):
        user_input('20020205')
    with pytest.raises(SystemExit):
        user_input('200202-05')
    with pytest.raises(SystemExit):
        user_input('2002-0205')

    # Test user_input() on input that is formatted in YYYY-MM-DD format, but has invalid days or months (i.e. a month that is not between 1 and 12).
    with pytest.raises(SystemExit):
        user_input('1999-00-25')
    with pytest.raises(SystemExit):
        user_input('1999-13-25')
    with pytest.raises(SystemExit):
        user_input('1999-07-00')
    with pytest.raises(SystemExit):
        user_input('1999-07-32')

# Test the find_difference() function, which finds the difference between a birthdate and today's date and then formats the output.
# Because the output changes every day with today's date, it is difficult to create tests that work everyday.
def test_find_difference():
    assert find_difference(date.today()) == 'Zero minutes'
