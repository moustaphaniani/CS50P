coin_value = False
amount_due = 50

while amount_due > 0:

    while coin_value == False:
    # Prompt the user to insert a coin of 50, 25, 10 or 5 cents
        coin = int(input("Please insert a coin at a time. Indicate the value of the coin : "))

        if coin == 5 or coin == 10 or coin == 25 or coin == 50:
            coin_value = True
        else:
            print("Amount Due:", amount_due)

    # Logic to output how many cents in change the user is owed
    amount_due = amount_due - coin

    if amount_due > 0:
        print("Amount Due:", amount_due)
    else:
        print("Change Owed:", abs(amount_due))

    coin_value = False
