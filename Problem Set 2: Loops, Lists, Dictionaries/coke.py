# Initially, the user has paid 0 cents
sum = 0

# While loop runs while the user has spent less than 50 cents
while sum < 50:

    # Tell the user how much more they have to spend.
    print('Amount Due:', 50 - sum)

    # Request the user to insert a 5-cent, 10-cent, or 25-cent coin.
    coin = int(input('Insert coin: '))
    if coin in [5,10,25]:
        sum = sum + coin
    else:
        pass

# When the while loop ends, the user must have spent more than 50 cents, so we print their change.
print('Change Owed:', sum - 50)
