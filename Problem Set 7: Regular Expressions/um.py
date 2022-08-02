import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # We are looking for instances in the string where “um” appears as a word unto itself, not as a substring of some other word.
    # \b matches at a position called a "word boundary" that has zero-length. The following three positions qualify as a word boundary:
    # 1. Before the first character in a string, if the first character is \w
    # 2. After the last character in the string if the last character is \w
    # 3. Between two characters in the string, where one is \w and the other is \W.
    # In essence, \b allows you to perform a "whole words only" search in the form \bword\b since \b matches the empty string at the beginning
    # or end of a word.
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)

    # findall returns a list of all of the matches. To get the number of matches, we take the length of said list.
    return len(matches)


if __name__ == "__main__":
    main()
