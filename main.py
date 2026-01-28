from pprint import pprint
from data import fetch_financials 

def main():
    print("Hello from valuationx!")
    from pprint import pprint
    pprint(fetch_financials.fetch_stock_financials("XOM"))

if __name__ == "__main__":
    main()
