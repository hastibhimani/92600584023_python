# Mutable object - List
numbers = list(map(int, input("Enter list values: ").split()))

print("Original list:", numbers)

new_value = int(input("Enter a new value for first element: "))
numbers[0] = new_value

print("Modified list:", numbers)

# Immutable object - Tuple
values = tuple(map(int, input("Enter tuple values: ").split()))

print("Original tuple:", values)

print("Tuple cannot be changed directly.")
