# Task 
# Let's try a classic Computer Science project: simple calculator program! 🔢
# Create a calculator.py program and define these five functions:

# add(a, b) that adds two numbers a and b.
# subtract(a, b) that subtracts two numbers a and b
# multiply(a, b) that multiplies two numbers a and b.
# divide(a, b) that divides two numbers a and b.
# exp(a, b) that takes a to the exponent (or power) of b.
# Make sure to return the result in each function definition.

# Test your calculator by calling each function once to make sure that it works!

# Code: 
def add(a, b):
  answer = a + b
  return answer 
def subtract(a, b):
  answer = a - b
  return answer 
def multiply(a, b):
  answer = a * b
  return answer
def divide(a, b):
  answer = a / b
  return answer 
def exp(a, b):
  answer = a ** b 
  return answer

print(add(2, 7))
print(subtract(10, 9))
print(multiply(25, 76))
print(divide(12, 4))
print(exp(2, 3))
