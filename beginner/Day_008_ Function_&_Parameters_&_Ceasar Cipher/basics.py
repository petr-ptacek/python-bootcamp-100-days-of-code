# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


# greet()


# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# greet_with_name("Joe Wick")


# Functions with more than 1 input

def greet_with(name: str, location: str):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# greet_with("Joe Wick", "Washington")

# Functions with keyword arguments

greet_with(name="Angela", location="London")
