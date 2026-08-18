# Tuple
values = tuple(map(int, input("Enter tuple values: ").split()))

print("Tuple:", values)
print("First element:", values[0])
print("Length of tuple:", len(values))

# Set
numbers = set(map(int, input("Enter set values: ").split()))

print("Set:", numbers)

add_value = int(input("Enter a value to add: "))
numbers.add(add_value)
print("After adding:", numbers)

remove_value = int(input("Enter a value to remove: "))

if remove_value in numbers:
    numbers.remove(remove_value)

print("After removing:", numbers)
