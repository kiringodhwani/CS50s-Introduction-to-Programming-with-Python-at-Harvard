**Assignments from Week 7 of CS50's Introduction to Programming with Python at Harvard**

Week 7 was spent learning about **Regular Expressions**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**working.py**: Expects a str as input in either of the following two 12-hour formats:  
<pre>
   9:00 AM to 5:00 PM  
   9 AM to 5 PM
</pre>
Then, returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expects that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Raises a ValueError instead if the input is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). Does not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).  
  
**test_working.py**: Testing file consisting of 6 functions that collectively test the convert() function in working.py. convert() is the function that expects a str in either of the above 12-hour formats and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**um.py**: Expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like hello, um, world, the function returns 1. Given text like yummy, though, the function returns 0.  
  
**test_um.py**: Testing file consisting of 5 functions that collectively test the count() function in um.py
