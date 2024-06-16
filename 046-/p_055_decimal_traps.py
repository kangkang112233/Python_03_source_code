import decimal

# Enable the trap for float operations in the decimal context
decimal.getcontext().traps[decimal.FloatOperation] = True


# Function to calculate total price using Decimal
def calculate_total_price(price, quantity):
    # Ensure price is a Decimal
    price_decimal = decimal.Decimal(price)
    # Calculate total price
    total_price = (
        price_decimal * quantity
    )  # This will raise an exception if quantity is not a Decimal
    return total_price


# Example book price and quantity
try:
    price = "19.99"  # Correct usage: string to Decimal
    quantity = decimal.Decimal("3")
    total_price = calculate_total_price(price, quantity)
    print(f"Total price for {quantity} books: {total_price}")
except decimal.FloatOperation as e:
    print(f"Float operation error: {str(e)}")
