numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)
print("First element:", numbers[0])
print("Slicing:", numbers[1:4])

numbers.append(int(input("Enter a number to add: ")))
print("After adding:", numbers)

squares = [x * x for x in numbers]
print("Squares:", squares)
