from um import count
import pytest

# Test input strings where there is an 'um' at the beginning of the string
def test_um_beginning():
    assert count('um') == 1
    assert count('Um') == 1
    assert count('um Hello') == 1
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('um um um, thanks') == 3

# Test input strings where there is an 'um' in the middle of the string
def test_um_middle():
    assert count(' um ') == 1
    assert count('.um.') == 1
    assert count('um um um') == 3
    assert count('I like to, um, eat food.') == 1
    assert count('Well, um, I do not um! Eat food, um? Too, um;  um often. ') == 5
    assert count('food um good um eat um yikes') == 3

# Test input strings where there is an 'um' at the end of the string
def test_um_end():
    assert count('Um') == 1
    assert count('um ') == 1
    assert count('thanks um, um...') == 2
    assert count('How about we eat some food, um!!!') == 1
    assert count('Well, um, that sounds good um !?') == 2

# Test input strings that contain 'um' as a part of some other word (i.e. 'um' is a substring of 'yummy')
# The program should only count instances where 'um' is a word unto itself, not a substring of some other word.
def test_substring():
    assert count('ummmmm') == 0
    assert count('Well, ummmmm') == 0
    assert count('yummy food') == 0
    assert count('Can I have some gum?') == 0
    assert count('I, um, want a plUm') == 1

