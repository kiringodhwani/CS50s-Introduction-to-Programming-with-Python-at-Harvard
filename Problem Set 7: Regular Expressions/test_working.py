from working import convert
import pytest


# Test that convert raises a ValueError when the input string has an invalid format
def test_invalid_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
    with pytest.raises(ValueError):
        convert('9 AM  5 PM')
    with pytest.raises(ValueError):
        convert('9:00 AM  5:00 PM')
    with pytest.raises(ValueError):
        convert('9AM to 5PM')
    with pytest.raises(ValueError):
        convert('9:00AM to 5:00PM')

# Test that convert raises a ValueError when the input string has a time with an invalid hour
def test_invalid_hour():
    with pytest.raises(ValueError):
        convert('0:00 AM  5:00 PM')
    with pytest.raises(ValueError):
        convert('13AM to 5PM')
    with pytest.raises(ValueError):
        convert('5AM to 24PM')
    with pytest.raises(ValueError):
        convert('4:00AM to 19:00PM')
    with pytest.raises(ValueError):
        convert('13:00AM to 3:00PM')

# Test that convert raises a ValueError when the input string has a time with an invalid minute value
def test_invalid_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('4:30AM to 7:90PM')
    with pytest.raises(ValueError):
        convert('9:70AM to 5:00PM')

# Test that convert behaves correctly with times in the twelfth hour (i.e. 12 AM and 12 PM)
def test_twelve():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12:45 AM to 12:09 PM') == '00:45 to 12:09'
    assert convert('12:05 AM to 12:53 PM') == '00:05 to 12:53'


# Test that convert behaves correctly with times with no minute value (i.e. '9 AM to 5 PM')
def test_no_minute():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('11 PM to 5 AM') == '23:00 to 05:00'

# Test that convert behaves correctly with times that have a minute value (i.e. '9:00 AM to 5:00 PM')
def test_with_minute():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('2:35 AM to 11:57 PM') == '02:35 to 23:57'
    assert convert('6:40 PM to 6:41 PM') == '18:40 to 18:41'
    assert convert('4:05 PM to 7:12 PM') == '16:05 to 19:12'
