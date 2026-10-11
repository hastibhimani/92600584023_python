import random

print("Random integer:", random.randint(1, 100))
print("Random float:", random.random())

numbers = [10, 20, 30, 40, 50]

print("Random choice:", random.choice(numbers))

random.shuffle(numbers)
print("Shuffled list:", numbers)
