import decimal

# Set the precision for Decimal calculations
decimal.getcontext().prec = 9


# Function to calculate the total price with tax using Decimal
def calculate_total_price(price, tax_rate):
    price_decimal = decimal.Decimal(price)
    tax_rate_decimal = decimal.Decimal(tax_rate)
    total_price = price_decimal * (1 + tax_rate_decimal)
    return total_price


# Example prices and tax rate
price = "19.9536"
tax_rate = "0.07"  # 7% tax rate

# Calculate total price with tax
total_price = calculate_total_price(price, tax_rate)

# Print the total price
print(f"Total price with tax: {total_price}")
