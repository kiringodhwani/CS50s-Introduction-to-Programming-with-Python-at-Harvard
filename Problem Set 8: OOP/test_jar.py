from jar import Jar
import pytest

def test_init():
    # Test default capacity
    jar1 = Jar()
    assert jar1.capacity == 12

    # Test with chosen sizes
    jar2 = Jar(1)
    assert jar2.capacity == 1
    jar3 = Jar(27)
    assert jar3.capacity == 27

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(50)

    # Try valid amounts to be deposited (i.e. don't add more cookies than the capacity)
    jar.deposit(8)
    assert jar.size == 8
    jar.deposit(17)
    assert jar.size == 25
    jar.deposit(12)
    assert jar.size == 37
    jar.deposit(5)
    assert jar.size == 42

    # Try invalid amounts
    with pytest.raises(ValueError):
        jar.deposit(9)
    with pytest.raises(ValueError):
        jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit(100)

    # Try maxing out the capacity
    jar.deposit(8)
    assert jar.size == 50
  
    # Extra Tests
    jar1 = Jar(50)
    with pytest.raises(ValueError):
        jar1.deposit(51)
    jar1.deposit(50)
    assert jar1.size == 50

def test_withdraw():
    # Test maxes
    jar1 = Jar(50)
    jar1.deposit(50)
    with pytest.raises(ValueError):
        jar1.withdraw(51)
    jar1.withdraw(50)
    assert jar1.size == 0

    jar2 = Jar(100)
    jar2.deposit(100)

    # Try valid amounts to be withdrawn
    jar2.withdraw(5)
    assert jar2.size == 95
    jar2.withdraw(59)
    assert jar2.size == 36
    jar2.withdraw(24)
    assert jar2.size == 12

    # Try invalid amounts to be withdrawn
    with pytest.raises(ValueError):
        jar2.withdraw(13)
    with pytest.raises(ValueError):
        jar2.withdraw(14)
    with pytest.raises(ValueError):
        jar2.withdraw(96)
