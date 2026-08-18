# No argument
def greet():
    print("Hello! Good Morning.")

# Positional arguments
def add(a, b):
    return a + b

# Default argument
def welcome(name="Student"):
    print("Welcome", name)


greet()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", add(a, b))

name = input("Enter your name: ")
welcome(name)
