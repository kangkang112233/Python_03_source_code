# Example of a Python class with a constructor method
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age, address):
        self.name = name  # Initialize name attribute
        self.age = age    # Initialize age attribute
        self.address = address  # Initialize address attribute

    # Method to display the person's details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


# Creating an instance of the Person class
person1 = Person("John Doe", 30, "123 Elm Street")
# Displaying the details of the created instance
person1.display_details()
