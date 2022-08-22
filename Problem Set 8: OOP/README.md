**Assignments from Week 8 of CS50's Introduction to Programming with Python at Harvard**

Week 6 was spent learning about **Object-Oriented Programming**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**seasons.py**: Prompts the user for their date of birth in YYYY-MM-DD format and then prints how old the user is in minutes, rounded to the nearest integer, using English words instead of numerals. Since a user might not know the time at which they were born, assumes, for simplicity, that the user was born at midnight (i.e., 00:00:00) on the inputted date. Also assumes that the current time is also midnight. In other words, even if the user runs the program at noon, assumes that it’s actually midnight, on the same date.

**test_seasons.py**: Testing file for seasons.py that tests both the find_difference() function and the user_input() function.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**jar.py**: Implements a cookie jar in which to store cookies. The Jar class has the following methods:
  
   - __init__ initializes a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If the capacity is not a non-negative int, though, __init__ instead raises a ValueError.
   - __str__ returns a str with n "🍪", where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str returns "🍪🍪🍪"
   - **deposit** adds n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit instead raises a ValueError.
   - **withdraw** removes n cookies from the cookie jar. If there aren’t that many cookies in the cookie jar, though, withdraw instead raises a ValueError.
   - **capacity** returns the cookie jar’s capacity.
   - **size** returns the number of cookies actually in the cookie jar.
  
**test_jar.py**: A testing file to test the methods of the Jar class.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**shirtificate.py**: Prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf. A CS50 shirtificate is a pdf that says "CS50 Shirtificate" at the top and then below it displays a red t-shirt that reads "[name] took CS50". The pdf has the following specifications:  
   - The orientation of the PDF is Portrait.  
   - The format of the PDF is A4, which is 210mm wide by 297mm tall.  
   - The top of the PDF is “CS50 Shirtificate” as text, centered horizontally.  
   - The shirt’s image is centered horizontally.  
   - The user’s name is on top of the shirt, in white text.  
   - Does not wrap long names across multiple lines.  


  
