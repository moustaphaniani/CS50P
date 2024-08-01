# Program that:
#
# Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
# Be sure to catch any exceptions, as with code.
# Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

import requests
import sys
import json

def main():
    while True:
        try:
            quantity = check_arg(sys.argv)
            if quantity > 0:
                response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
                json_dict = response.json()
                btc_value = float(json_dict['bpi']['USD']['rate_float'])
                amount = quantity * btc_value
                print(f"${amount:,.4f}")
                break
        except requests.RequestException:
            sys.exit(1)

def check_arg(arg):
    # Check if 1 argument is passed. Otherwise print "Missing command-line argument" and break
    if len(arg) == 2:
        # Check if the argument passed is a float. Otherwise print "Command-line argument is not a number" and break
        if arg[1].isnumeric() or '.' in arg[1]:
            return float(arg[1])
        else:
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)


if __name__ == "__main__":
    main()
