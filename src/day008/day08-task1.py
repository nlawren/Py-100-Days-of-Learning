# Simple Function
def greet():
    print("Hello Fred")
    print("How do you do James?")
    print("Isn't the weather nice today?")


greet()


# Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("James Fred")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "James Fred")


# Calling greet_with() with Keyword Arguments
greet_with(location="Berlin", name="Fred")
