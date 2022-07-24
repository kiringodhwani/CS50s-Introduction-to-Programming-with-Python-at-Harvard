from twttr import shorten

# Testing cases where the input is one word consisting of many vowels
def test_vowels():
    assert shorten('paeiouyp') == 'pyp'
    assert shorten('adoulie') == 'dl'
    assert shorten('eucosia') == 'cs'
    assert shorten('aeiou') == ''

# Testing cases where the input is one letter
def test_one_char():
    assert shorten('a') == ''
    assert shorten('i') == ''
    assert shorten('o') == ''
    assert shorten('u') == ''
    assert shorten('e') == ''
    assert shorten('c') == 'c'
    assert shorten('z') == 'z'

# Testing cases where the input has only consonants
def test_consonants():
    assert shorten('bcdkhgdghshy') == 'bcdkhgdghshy'
    assert shorten('twttr') == 'twttr'
    assert shorten('hyphyntfd') == 'hyphyntfd'

# Testing cases where the input is a sentence
def test_sentence():
    assert shorten('I eat a sandwich for dinner. Yum!') == ' t  sndwch fr dnnr. Ym!'
    assert shorten('Burgers are a yummy type of food.') == 'Brgrs r  ymmy typ f fd.'
    assert shorten('I am a college student at Tufts.') == ' m  cllg stdnt t Tfts.'

# Testing cases where the input contains many non-letter characters
def test_weird_characters():
    assert shorten('       %  2  a 4 5 6') == '       %  2   4 5 6'
    assert shorten('        ') == '        '
    assert shorten('130393aaa82**#&#&$*') == '13039382**#&#&$*'
    assert shorten('!?><;:.,+=_-') == '!?><;:.,+=_-'
    assert shorten('aA1bB2cC3dD4Ee5fF6Uu7Ii8Po9Oo10') == '1bB2cC3dD45fF678P910'
