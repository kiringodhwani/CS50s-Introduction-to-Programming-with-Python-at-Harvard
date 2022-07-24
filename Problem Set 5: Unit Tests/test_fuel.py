from fuel import convert, gauge
import pytest

# Tests to make sure that convert() throws a ZeroDivisionError if the denominator of the fraction is 0
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')
    with pytest.raises(ZeroDivisionError):
        convert('0/0')
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

# Tests to make sure that convert() throws a ValueError when the numerator of the fraction is greater than the denominator
def test_value_error():
    with pytest.raises(ValueError):
        convert('11/10')
    with pytest.raises(ValueError):
        convert('1001/1000')
    with pytest.raises(ValueError):
        convert('2/1')

# Tests to make sure that convert() throws a ValueError when the user-inputted numerator / denom. aren't integers
def test_value_error():
    with pytest.raises(ValueError):
        convert('three/four')
    with pytest.raises(ValueError):
        convert('cat/4')
    with pytest.raises(ValueError):
        convert('12/bigbird')
    with pytest.raises(ValueError):
        convert('100.7/236.58')
    with pytest.raises(ValueError):
        convert('1.5/3')
    with pytest.raises(ValueError):
        convert('1/4.4')

# Tests to make sure that the upper bound of the percentage value returned by convert() is in fact 100 and the lower bound is in fact 0
def test_bounds():
    assert convert('1/1') == 100
    assert convert('0/1') == 0
    assert convert ('1234/1234') == 100
    assert convert('0/1000') == 0

    # Testing rounding cases
    assert convert('5000/5001') == 100
    assert convert('1/10000') == 0
    assert convert('999/1000') == 100
    assert convert('1/2000') == 0

# Testing convert on general cases (i.e. valid fractions (X/Y) where X > Y and Y != 0)
def test_convert_general():
    # Rounding required
    assert convert('2/3') == 67
    assert convert('95/111') == 86
    assert convert('8/9') == 89
    assert convert('1/6') == 17

    # Rounding not required
    assert convert('1/3') == 33
    assert convert('297/356') == 83
    assert convert('3/4') == 75
    assert convert('4/9') == 44

# Tests to make sure that gauge() returns 'E' when provided an integer less than or equal to 1
# Note: Because of the exceptions thrown by convert() and because convert() always returns
#       an integer (which is then passed into gauge as a parameter), there is no need to test
#       gauge with non-integers and there is no need to test gauge with integers less than 0.
def test_empty():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'

# Tests to make sure that gauge() returns 'F' when provided an integer greater than or equal to 99
# Note: Because of the exceptions thrown by convert() and because convert() always returns
#       an integer (which is then passed into gauge as a parameter), there is no need to test
#       gauge with non-integers and there is no need to test gauge with integers greater than 100.
def test_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

# Tests to make sure that when gauge() is provided an integer Z, where 1 < Z < 99, returns "Z%"
# Note: Because convert() always returns an integer (which is then passed into gauge as a parameter),
#       there is no need to test gauge with non-integers.
def test_percentage():
    assert gauge(2) == '2%'
    assert gauge(98) == '98%'
    assert gauge(93) == '93%'
    assert gauge(75) == '75%'
    assert gauge(17) == '17%'
    assert gauge(33) == '33%'
    assert gauge(6) == '6%'
    assert gauge(51) == '51%'

