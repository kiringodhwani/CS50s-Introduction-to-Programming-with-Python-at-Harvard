**Assignments from Week 5 of CS50's Introduction to Programming with Python at Harvard**

Week 5 was spent learning about **Unit Testing**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**twttr.py**: Prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.  
  
**test_twttr.py**: Testing file consisting of 5 functions that collectively test the shorten() function in twttr.py. Testing cases include (but are not limited to): strings with all vowels, strings with all consonants, strings with non-letter characters, strings that consist of an entire sentence.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**bank.py**: Prompts the user for a greeting. If the greeting starts with “hello”, outputs $0. If the greeting starts with an “h” (but not “hello”), outputs $20. Otherwise, outputs $100. Treats the user’s greeting case-insensitively.
  
**test_bank.py**: Testing file consisting of 3 functions that collectively test the value() function in bank.py. Tests the case-insensitivity of the value() function (e.g. 'Hello' and 'hello' should result in the same response) and tests the program's ability to correctly determine when each of 0, 20, and 100 should be returned.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**plates.py**: Prompts the user for a vanity plate and then outputs **valid** if the plate meets all of the requirements of a vanity plate
and **invalid** if it does not meet all of the requirements. The requirements of a vanity plate are as follows:
   - All vanity plates must start with at least two letters.”
   - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
   - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
   - “No periods, spaces, or punctuation marks are allowed.”
  
**test_plates.py**: Testing file consisting of 5 functions that collectively test the is_valid() function in plates.py. First function tests that the program fails plates that do not have between 2 and 6 characters (letters or numbers) inclusive. Second function tests that program fails all plates that do not start with at least 2 letters. Third function tests that the program fails all plates that have numbers in the middle of the plate sequence. Fourth function tests that the program fails all plates where the first number used is ‘0’. Fifth and final function tests that the program fails all plates that contain periods, spaces, or punctuation.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**adieu.py**: 
