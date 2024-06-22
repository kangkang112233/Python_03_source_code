import statistics

# Example book ratings
book_ratings = [4.5, 4.0, 5.0, 3.5, 4.0, 3.0, 2.5, 4.5, 5.0, 3.5]

# Calculate the quartiles of book ratings
quartiles = statistics.quantiles(book_ratings, n=4)
print(f"Quartiles: {quartiles}")

# Calculate the deciles of book ratings
deciles = statistics.quantiles(book_ratings, n=10)
print(f"Deciles: {deciles}")
