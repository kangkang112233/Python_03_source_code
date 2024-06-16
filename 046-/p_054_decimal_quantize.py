from decimal import Decimal, getcontext, ROUND_UP

# Set the context for Decimal operations
getcontext().prec = 3  # Set precision to 3 decimal places


# Function to round book prices
def round_book_price(price, precision):
    # Create a Decimal object for the price
    price_decimal = Decimal(price)
    # Create a Decimal object for the precision
    precision_decimal = Decimal(precision)
    # Round the price using the quantize method
    rounded_price = price_decimal.quantize(precision_decimal, rounding=ROUND_UP)
    return rounded_price


# Example book price and precision
price = "19.99"
precision = "0.1"  # Round to the nearest tenth

# Round the book price
rounded_price = round_book_price(price, precision)

# Print the rounded price
print(f"Rounded Price: {rounded_price}")
