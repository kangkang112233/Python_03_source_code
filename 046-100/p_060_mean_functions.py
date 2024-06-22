import statistics

# Example book ratings
book_ratings = [4.5, 4.0, 5.0, 3.5, 4.0]

# Calculate the arithmetic mean of book ratings
arithmetic_mean_rating = statistics.mean(book_ratings)
print(f"Arithmetic Mean Rating: {arithmetic_mean_rating}")

# Calculate the geometric mean of book ratings
geometric_mean_rating = statistics.geometric_mean(book_ratings)
print(f"Geometric Mean Rating: {geometric_mean_rating}")

# Calculate the harmonic mean of book ratings
harmonic_mean_rating = statistics.harmonic_mean(book_ratings)
print(f"Harmonic Mean Rating: {harmonic_mean_rating}")
