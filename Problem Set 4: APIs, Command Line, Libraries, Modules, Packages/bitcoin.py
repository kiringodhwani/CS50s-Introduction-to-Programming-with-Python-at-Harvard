import sys
import requests

# Along with the filename, the program expects the user to specify as a command-line argument the number of Bitcoins that they would like to buy.
if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

# If the bitcoin argument cannot be converted to a float, the program exits and prints an error message
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

# Query the API for the CoinDesk Bitcoin Price Index and catch any exceptions
try:
    # Query the API for the CoinDesk Bitcoin Price Index at to return a JSON object
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # Convert response to JSON format
    o = response.json()

    # Access the nested key in the JSON that corresponds with the current price of Bitcoin in USD as a float
    price = float(o['bpi']['USD']['rate_float'])

except requests.RequestException:
    sys.exit()

# Calculate the current cost of n bitcoins
cost_of_n = n * price

# Format the cost to 4 decimal places and then print
print(f"${cost_of_n:,.4f}")
