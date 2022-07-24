**Assignments from Week 5 of CS50's Introduction to Programming with Python at Harvard**

Week 5 was spent learning about **Unit Testing**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
1. **professor.py**: 
   - Prompts the user for a level (either 1, 2, or 3). If the user does not input 1, 2, or 3, the program re-prompts the user.
   - Randomly generates ten math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with "level" digits (i.e. the number of digits in each of the randomly generated numbers is equal to the level).
   - Prompts the user to solve each of the math problems. If an answer is not correct (or not even a number), the program outputs EEE and prompts the user again, allowing the user up to three tries in total per problem. If the user has still not answered correctly after three tries, the program outputs the correct answer and moves on to the next problem.
   - Ultimately outputs the user’s score (i.e. the number of problems they got correct out of 10).
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
2. **bitcoin.py**: 
   - Expects the user to specify as a command-line argument the number of Bitcoins, 'n', that they would like to buy.
   - Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
   - Outputs the current cost of 'n' Bitcoins in USD to four decimal places, using commas (',') as a thousands separator.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
3. **figlet.py**: Uses FIGlet to allow users to print out messages in FIGlet fonts:
   - Expects zero or two command-line arguments:
      - Zero if the user would like to output text in a random FIGlet font.
      - Two if the user would like to output text in a specific FIGlet font, in which case the first of the two command line arguments should be -f or --font, and the second of the two should be the name of the FIGlet font.
   - Prompts the user for a str of text.
   - Outputs that text in the desired FIGlet font.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**adieu.py**: 
