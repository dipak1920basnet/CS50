import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        bit_coin = sys.argv[1]
        bit_coin = float(bit_coin)
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Failed to get requests")
else:
    # print(f"bit-coin: {bit_coin}")
    pretty_json = response.json()
    t = pretty_json['bpi']['USD']['rate_float']
    bit_coin_price = t*bit_coin
    # print(t)
    print(f"${bit_coin_price:,.4f}")

