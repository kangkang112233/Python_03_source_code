import math


# Function to check and clean book prices
def clean_book_prices(prices):
    cleaned_prices = []
    for price in prices:
        if math.isnan(price):
            cleaned_prices.append(0.0)  # Replace NaN with 0.0
        else:
            cleaned_prices.append(price)
    return cleaned_prices


# Example list of book prices, including a NaN value
book_prices = [19.95, 15.99, float("nan"), 23.50]

# Clean the book prices
cleaned_prices = clean_book_prices(book_prices)

# Print the cleaned prices
print("Cleaned Prices:")
for price in cleaned_prices:
    print(f"${price:0.2f}")
