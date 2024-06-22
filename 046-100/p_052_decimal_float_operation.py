import decimal

# Set the precision for Decimal calculations
decimal.getcontext().prec = 4


# Function to calculate total price including tax using Decimal
def calculate_total_price(price, tax_rate):
    # Convert float tax rate to Decimal
    tax_rate_decimal = decimal.Decimal(str(tax_rate))
    # Calculate tax amount
    tax_amount = decimal.Decimal(price) * tax_rate_decimal
    # Calculate total price
    total_price = decimal.Decimal(price) + tax_amount
    return total_price


# Example price and tax rate
price = "19.99"  # Price of the book as string to avoid float precision issues
tax_rate = 0.07  # 7% tax rate

# Calculate total price including tax
total_price = calculate_total_price(price, tax_rate)

# Print the total price
print(f"Total price including tax: {total_price}")
