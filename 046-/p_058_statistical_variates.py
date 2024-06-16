import random


# Function to generate book prices based on normal distribution
def generate_book_prices(mu, sigma, count):
    prices = [round(random.normalvariate(mu, sigma), 2) for _ in range(count)]
    return prices


# Function to generate demand based on gamma distribution
def simulate_book_demand(k, theta, count):
    demands = [round(random.gammavariate(k, theta)) for _ in range(count)]
    return demands


# Example usage
mu, sigma = 20.0, 5.0  # Mean price $20, standard deviation $5
k, theta = 2.0, 5.0  # Shape parameter 2, scale parameter 5
count = 5  # Number of books

# Generate book prices
book_prices = generate_book_prices(mu, sigma, count)

# Simulate book demand
book_demands = simulate_book_demand(k, theta, count)

# Print results
print("Generated Book Prices:", book_prices)
print("Simulated Book Demands:", book_demands)
