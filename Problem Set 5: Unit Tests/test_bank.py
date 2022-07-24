from bank import value

# Testing that the program outputs '$0' if the greeting starts with 'hello'
def test_zero():
    # General case(s) with capital first letter
    assert value('Hello') == 0
    assert value('Hello, Newman') == 0

    # General case(s) with lowercase first letter
    assert value('hello') == 0
    assert value('hello, Newman') == 0

    # Hello part, but not all, of first word
    assert value('Hellonewman') == 0
    assert value('hellonewman') == 0
    assert value('Hellooooooo') == 0
    assert value('hellooooooooo') == 0

    assert value('Helooooooo') == 20
    assert value('helooooooooo') == 20

# Testing that the program outputs '$20' if the greeting starts with an 'h' (but not 'hello')
def test_20_dollars():
    # General case(s) with capital first letter
    assert value('Hi') == 20
    assert value('Hey, Newman') == 20
    assert value('Hdkljaskldjaksdja') == 20
    assert value('Hows it going?') == 20

    # General case(s) with lowercase first letter
    assert value('hi') == 20
    assert value('hey, Newman') == 20
    assert value('hdkljaskldjaksdja') == 20
    assert value('hows it going?') == 20

# Testing that the program outputs '$100' if the greeting does not start with an 'h'
def test_100_dollars():
    # General case(s) with capital first letter
    assert value('Whats happening?') == 100
    assert value('Yellow') == 100

    # General case(s) with lowercase first letter
    assert value('whats happening?') == 100
    assert value('yellow') == 100

