"""
CodeAlpha - Python Programming Internship
Task 2: Stock Portfolio Tracker

Lets the user enter stock names and quantities, looks up hardcoded
prices, and calculates the total investment value. Optionally saves
the result to a .txt or .csv file.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 178,
    "MSFT": 420,
    "NFLX": 640,
    "META": 480,
}


def show_available_stocks():
    print("\nAvailable stocks and prices (per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio():
    """Ask the user for stock symbols and quantities until they're done."""
    portfolio = {}  # symbol -> quantity

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our price list. Try one of: {', '.join(STOCK_PRICES)}\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """Return a list of (symbol, quantity, price, subtotal) rows and the grand total."""
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * quantity
        rows.append((symbol, quantity, price, subtotal))
        total += subtotal
    return rows, total


def print_summary(rows, total):
    print("\n----- Portfolio Summary -----")
    print(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Subtotal':<10}")
    for symbol, quantity, price, subtotal in rows:
        print(f"{symbol:<8}{quantity:<6}${price:<9}${subtotal:<9}")
    print("-" * 34)
    print(f"Total Investment Value: ${total}\n")


def save_to_file(rows, total):
    choice = input("Save results to a file? (y/n): ").strip().lower()
    if choice != "y":
        return

    file_format = input("Choose format - txt or csv: ").strip().lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Subtotal"])
            writer.writerows(rows)
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total])
        print(f"Saved to {filename}")
    else:
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("Portfolio Summary\n")
            f.write(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Subtotal':<10}\n")
            for symbol, quantity, price, subtotal in rows:
                f.write(f"{symbol:<8}{quantity:<6}${price:<9}${subtotal:<9}\n")
            f.write(f"\nTotal Investment Value: ${total}\n")
        print(f"Saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    rows, total = calculate_investment(portfolio)
    print_summary(rows, total)
    save_to_file(rows, total)


if __name__ == "__main__":
    main()
