from numb3rs import validate

import pytest

def test_invalid():
    assert validate('cat') == False
    assert validate('1.2.3.cat') == False
    assert validate('1.2.3.4.5') == False
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False
    assert validate('1..2..3..4') == False
    assert validate('1..2.3.4') == False
    assert validate('-1.3.2.5') == False

def test_bounds():
    assert validate('0.50.150.255') == True
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('256.256.256.256') == False
    assert validate('1.1.1.256') == False
    assert validate('1.1.256.1') == False
    assert validate('1.256.1.1') == False
    assert validate('256.1.1.1') == False

