# Define a function with default parameter values
def add_book(title, author, published_year=2021, genre="Fiction"):
    # This function adds a book to the library system
    print(f"Adding book: Title='{title}', Author='{author}', Published Year={published_year}, Genre='{genre}'")


# Correct usage with all parameters specified
add_book("1984", "George Orwell", 1949, "Dystopian")
# Output: Adding book: Title='1984', Author='George Orwell', Published Year=1949, Genre='Dystopian'

# Correct usage with default parameters
add_book("To Kill a Mockingbird", "Harper Lee")
# Output: Adding book: Title='To Kill a Mockingbird', Author='Harper Lee', Published Year=2021, Genre='Fiction'

# Incorrect usage with a missing default parameter
try:

    def incorrect_function(param1, param2=5, param3):
        pass


except SyntaxError as e:
    print("Error:", e)
# Output: Error: non-default argument follows default argument
