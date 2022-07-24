**Assignments from Week 5 of CS50's Introduction to Programming with Python at Harvard**

Week 5 was spent learning about **Unit Testing**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**fuel.py**: Prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, outputs E instead to indicate that the tank is essentially empty. And if 99% or more remains, outputs F instead to indicate that the tank is essentially full. If X or Y is not an integer, X is greater than Y, or Y is 0, instead prompts the user again. Contains **convert()** and **gauge()**:
  
- **convert()** expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert raises a ValueError. If Y is 0, then convert raises a ZeroDivisionError.
- **gauge()** expects an int and returns a str that is:
   - "E" if that int is less than or equal to 1,
   - "F" if that int is greater than or equal to 99,
   - and "Z%" otherwise, wherein Z is that same int.
  
**test_fuel.py**: Testing file consisting of 5 functions that collectively test the convert() function in fuel.py and 3 functions that collectively test the gauge function in fuel.py:
1. The first function tests that convert() throws a ZeroDivisionError if the denominator of the fraction (Y) is 0.
2. The second function tests that convert() throws a ValueError when the numerator of the fraction (X) is greater than the denominator (Y).
3. The third function tests that convert() throws a ValueError when the user-inputted numerator (X) and/ or denominator (Y) aren't integers.
4. The fourth function tests that the upper bound of the percentage value returned by convert() is in fact 100 and the lower bound is in fact 0.
5. The fifth function tests convert() on general cases (i.e. valid fractions (X/Y) where X > Y, Y != 0, and X and Y are integers).
6. The sixth function tests that gauge() returns 'E' when provided an integer less than or equal to 1.
7. The seventh function tests that gauge() returns 'F' when provided an integer greater than or equal to 99.
8. The eighth function tests that when gauge() is provided an integer Z, where 1 < Z < 99, it returns "Z%".
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**plates.py**: Prompts the user for a vanity plate and then outputs **valid** if the plate meets all of the requirements of a vanity plate
and **invalid** if it does not meet all of the requirements. The requirements of a vanity plate are as follows:
   - All vanity plates must start with at least two letters.”
   - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
   - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
   - “No periods, spaces, or punctuation marks are allowed.”  
  
Contains is_valid(), which expects a str as input (a vanity plate) and returns True if that str meets all of the vanity plate requirements and False if it does not.  
  
**test_plates.py**: Testing file consisting of 5 functions that collectively test the is_valid() function in plates.py:  
1. First function tests that the program fails plates that do not have between 2 and 6 characters (letters or numbers) inclusive.
2. Second function tests that program fails all plates that do not start with at least 2 letters. 
3. Third function tests that the program fails all plates that have numbers in the middle of the plate sequence. 
4. Fourth function tests that the program fails all plates where the first number used is ‘0’. 
5. Fifth and final function tests that the program fails all plates that contain periods, spaces, or punctuation.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**twttr.py**: Prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. Contains shorten(), which expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
  
**test_twttr.py**: Testing file consisting of 5 functions that collectively test the shorten() function in twttr.py. Testing cases on test_twttr.py include (but are not limited to): strings with all vowels, strings with all consonants, strings with non-letter characters, strings that consist of an entire sentence.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**bank.py**: Prompts the user for a greeting. If the greeting starts with “hello”, outputs $0. If the greeting starts with an “h” (but not “hello”), outputs $20. Otherwise, outputs $100. Contains value(), which expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. 
  
**test_bank.py**: Testing file consisting of 3 functions that collectively test the value() function in bank.py. The 3 tests on test_bank.py test the case-insensitivity of the value() function (e.g. 'Hello' and 'hello' should result in the same response) and test the program's ability to correctly determine when each of 0, 20, and 100 should be returned.
  

  

