import requests
import sys

api = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    try:
        q = requests.get(api)
        xz = q.json()
        yz = xz["bpi"]["USD"]["rate_float"]
        price = yz * argument()
        print(f"${price:,.4f}")
    except requests.RequestException:
        print("Error")
        quit()

def argument():
    try:
        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
        else:
            return float(sys.argv[1])
    except (ValueError, TypeError):
        print("Command-line argument is not a number")
        sys.exit(1)

if __name__ == "__main__":
    main()

