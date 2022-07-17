**Assignments from Week 3 of CS50's Introduction to Programming with Python at Harvard**

Week 3 was spent learning about **Loops (for and while), Lists, and Dictionaries**. Below are descriptions of each of the programs in this folder:

1. **outdated.py**: Prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:  
[  
    "January",  
    "February",  
    "March",  
    "April",  
    "May",  
    "June",  
    "July",  
    "August",  
    "September",  
    "October",  
    "November",  
    "December"  
]  
Then outputs the same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format (9/8/1636 or September 8, 1636), prompts the user again. Assumes that every month has no more than 31 days (i.e. does not validate whether a month has 28, 29, 30, or 31 days). Re-prompts the user when they input a date with a non-4-digit year, a day not between 1 and 31, and a month not between 1 and 12.  
2. **fuel.py**: Prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, outputs E instead to indicate that the tank is essentially empty. And if 99% or more remains, outputs F instead to indicate that the tank is essentially full. If X or Y is not an integer, X is greater than Y, or Y is 0, instead prompts the user again. Catches ValueErrors and ZeroDivisionErrors.  
3. **taqueria.py**: Enables a user to place orders from the below dict/menu of entrees:
{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Prompts the user for items (entrees), one per line, until the user inputs control-d. After each inputted item, displays the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treats the user’s input case insensitively. Ignores any input that isn’t an item. Assumes that every item on the menu will be titlecased.  
4. **grocery.py**: Prompts the user for items (meant to be items from a grocery store), one per line, until the user inputs control-d. Then outputs the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. Does not pluralize items. Treats the user’s input case-insensitively.
