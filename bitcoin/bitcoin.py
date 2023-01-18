import sys
import requests
import json

req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
response = req.json()
text = json.dumps(response, indent = 4)

bitcoin_price_now = response["bpi"]["USD"]["rate_float"]

try:
    n = float(sys.argv[1])
except:
    if len(sys.argv) == 2:
        sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

amount = n * bitcoin_price_now

print(f"${amount:,.4f}")

