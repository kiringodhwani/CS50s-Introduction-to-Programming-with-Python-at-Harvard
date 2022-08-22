**Assignments from Week 8 of CS50's Introduction to Programming with Python at Harvard**

Week 6 was spent learning about **Object-Oriented Programming**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**seasons.py**: Prompts the user for their date of birth in YYYY-MM-DD format and then prints how old the user is in minutes, rounded to the nearest integer, using English words instead of numerals. Since a user might not know the time at which they were born, assumes, for simplicity, that the user was born at midnight (i.e., 00:00:00) on the inputted date. Also assumes that the current time is also midnight. In other words, even if the user runs the program at noon, assumes that it’s actually midnight, on the same date.

**test_seasons.py**: Testing file for seasons.py that tests both the find_difference() function and the user_input() function.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**shirt.py**: Implements a cookie jar in which to store cookies. The Jar class has the following methods:
  
   - __init__ initializes a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If the capacity is not a non-negative int, though, __init__ instead raises a ValueError.
   - __str__ returns a str with n "🍪", where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str returns "🍪🍪🍪"
   - **deposit** adds n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit instead raises a ValueError.
   - **withdraw** removes n cookies from the cookie jar. If there aren’t that many cookies in the cookie jar, though, withdraw instead raises a ValueError.
   - **capacity** returns the cookie jar’s capacity.
   - **size** returns the number of cookies actually in the cookie jar.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**pizza.py**: Expects exactly one command-line argument other than the filename --- the name (or path) of a CSV file in Pinocchio's format. Here is an example of a pizza menu in said format:
  <pre>
   Sicilian Pizza,Small,Large  
   Cheese,$25.50,$39.95  
   1 item,$27.50,$41.95  
   2 items,$29.50,$43.95  
   3 items,$31.50,$45.95  
   Special,$33.50,$47.95  
  </pre>
Then, outputs the data from the input CSV as a table formatted as ASCII art using the 'tabulate' package. Below is the resulting output of the above pizza menu:
  <pre>
   +------------------+---------+---------+  
   | Sicilian Pizza   | Small   | Large   |  
   +==================+=========+=========+  
   | Cheese           | $25.50  | $39.95  |  
   +------------------+---------+---------+  
   | 1 item           | $27.50  | $41.95  |  
   +------------------+---------+---------+  
   | 2 items          | $29.50  | $43.95  |  
   +------------------+---------+---------+  
   | 3 items          | $31.50  | $45.95  |  
   +------------------+---------+---------+  
   | Special          | $33.50  | $47.95  |  
   +------------------+---------+---------+  
  </pre>
NOTE: If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program instead exits via sys.exit.  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**lines.py**: Expects exactly one command-line argument other than the filename, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.  
  
NOTE: If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
  
NOTE: Assumes that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assumes that any line that only contains whitespace is blank.
