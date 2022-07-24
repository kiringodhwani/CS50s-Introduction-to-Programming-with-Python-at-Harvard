from plates import is_valid

# Tests to make sure that the program fails plates that do not between 2 and 6 characters (letters or numbers) inclusive.
def test_length():
    # Less than 2 characters
    assert is_valid('A') == False
    assert is_valid('2') == False
    assert is_valid('') == False

    # Exactly 2 characters
    assert is_valid('BB') == True

    # Exactly 6 characters
    assert is_valid('CCCCCC') == True

    # More than 6 characters
    assert is_valid('DDDDDDD') == False
    assert is_valid('Ejdalksdaklsdjad') == False

# Tests to make sure that the program fails all plates that do not start with at least 2 letters
def test_first_two_letters():
    # Two numbers out of first two
    assert is_valid('12') == False
    assert is_valid('21') == False
    assert is_valid('93AJB') == False
    assert is_valid('67JDN') == False

    # One letter out of first two
    assert is_valid('1A') == False
    assert is_valid('2B') == False
    assert is_valid('1AKAJS') == False
    assert is_valid('A1SKJDD') == False
    assert is_valid('1ABCDE') == False
    assert is_valid('H2IJKL') == False

    # Two letters out of first two
    assert is_valid('XY') == True
    assert is_valid('JK') == True
    assert is_valid('XY1892') == True
    assert is_valid('JK1') == True

    # All letters (more than 2 characters)
    assert is_valid('ABC') == True
    assert is_valid('TUVWXY') == True

    # Two letters, then numbers
    assert is_valid('AB1234') == True
    assert is_valid('LM9876') == True

# Tests to make sure that the program fails plates that have numbers in the middle; numbers must come at the end.
def test_numbers_middle():
    # Numbers at the end of the plate
    assert is_valid('AB1') == True
    assert is_valid('ABC1') == True
    assert is_valid('ABCD1') == True
    assert is_valid('ABCDE1') == True
    assert is_valid('AAA222') == True
    assert is_valid('AA2222') == True
    assert is_valid('BC24') == True
    assert is_valid('JK456') == True
    assert is_valid('JKQ456') == True
    assert is_valid('JKJDJ1') == True

    # Numbers in the middle of the plate
    assert is_valid('AB1C') == False
    assert is_valid('AB2CD') == False
    assert is_valid('AB3CDE') == False
    assert is_valid('ABC1D') == False
    assert is_valid('ABC1DE') == False
    assert is_valid('ABCD1E') == False
    assert is_valid('AB555D') == False
    assert is_valid('ABC55D') == False
    assert is_valid('AB55D') == False
    assert is_valid('AAA22A') == False

# Tests to make sure that the program fails all plates where the first number used is ‘0’.
def test_0_first():
    # 0 first
    assert is_valid('AA0') == False
    assert is_valid('AAA0') == False
    assert is_valid('AAAA0') == False
    assert is_valid('AAAAA0') == False
    assert is_valid('AA01') == False
    assert is_valid('AA012') == False
    assert is_valid('AA0123') == False

    # 0 included but not first
    assert is_valid('AA10') == True
    assert is_valid('AA1000') == True
    assert is_valid('AA1011') == True
    assert is_valid('AA1101') == True
    assert is_valid('AAA10') == True
    assert is_valid('AAA100') == True

# Tests to make sure that the program fails all plates that contain periods, spaces, or punctuation
def test_punctuation():
    # periods
    assert is_valid('AA.') == False
    assert is_valid('AAA.') == False
    assert is_valid('AAAA.') == False
    assert is_valid('AAAAA.') == False
    assert is_valid('AA....') == False
    assert is_valid('AA...A') == False
    assert is_valid('AA..AA') == False
    assert is_valid('AA.AAA') == False

    # spaces and punctuation
    assert is_valid('AA  AA') == False
    assert is_valid('AA   A') == False
    assert is_valid('AA   ') == False
    assert is_valid('AA?') == False
    assert is_valid('AA!') == False
    assert is_valid('AA,') == False
    assert is_valid('AA.') == False
    assert is_valid('AA.?,;') == False
    assert is_valid('AA_:><') == False
