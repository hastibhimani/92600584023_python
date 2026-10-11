
#Import entire module
import math
print("Square root:", math.sqrt(25))

#Import a specific function
from math import factorial
print("Factorial:", factorial(5))

#Import module with an alias
import math as m
print("Power:", m.pow(2, 3))

#Import multiple functions
from math import sin, cos
print("sin(0):", sin(0))
print("cos(0):", cos(0))
