import decimal

# Set the precision for Decimal calculations
decimal.getcontext().prec = 4  # Set precision to 4 decimal places


# Function to calculate the price after discount using Decimal
def calculate_discounted_price(original_price, discount_rate):
    # Convert inputs to Decimal with the specified precision
    original_price = decimal.Decimal(original_price)
    discount_rate = decimal.Decimal(discount_rate)
    # Calculate the discount
    discount = original_price * (discount_rate / decimal.Decimal("100"))
    # Calculate the final price
    final_price = original_price - discount
    return final_price


# Original price and discount rate
original_price = "19.99"
discount_rate = "15"  # 15% discount

# Calculate the discounted price
discounted_price = calculate_discounted_price(original_price, discount_rate)

# Print the discounted price
print(f"Discounted price: {discounted_price}")
