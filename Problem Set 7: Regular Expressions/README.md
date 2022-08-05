**Assignments from Week 7 of CS50's Introduction to Programming with Python at Harvard**

Week 7 was spent learning about **Regular Expressions**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**working.py**: Expects a str as input in either of the following two 12-hour formats:  
<pre>
   9:00 AM to 5:00 PM  
   9 AM to 5 PM
</pre>
Then, returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expects that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Raises a ValueError instead if the input is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). Does not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).  
  
**test_working.py**: Testing file consisting of 6 functions that collectively test the convert() function in working.py. convert() is the function in working.py that expects a str in either of the above 12-hour formats and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**um.py**: Expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like "hello, um, world", the function returns 1. Given text like "yummy", though, the function returns 0.  
  
**test_um.py**: Testing file consisting of 4 functions that collectively test the count() function in um.py count() is the function in um.py that that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**numb3rs.py**: An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive.
  
numb3rs.py expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
  
**test_numb3rs.py**: Testing file consisting of 2 functions that collectively test the validate() function in numb3rs.py. validate() is the function in numb3rs.py that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**watch.py**: Expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expects that any such URL will be in one of the formats below. Assumes that the value of src will be surrounded by double quotes. And assumes that the input will contain no more than one such URL. If the input does not contain any such URL at all, returns None.
<pre>
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
</pre>
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
