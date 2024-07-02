# Task 
# When you go to a drive-thru like McDonald's, you can order food using the item numbers. For example, a Happy Meal might be a #3!
# Create a drive_thru.py program with your favorite fast food chain's menu.
# Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!
# For example, if you called the function with:

# Argument value 1, it could return '🍔 Cheeseburger'.
# Argument value 2, it could return '🍟 Fries'.
# Argument value 3, it could return '🥤 Soda'.
# Argument value 4, it could return '🍦 Ice Cream'.
# Argument value 5, it could return '🍪 Cookie'.
# Make sure to call this function a few times to make sure that it works!

# Lastly, let's do the following:
# Create a welcome menu and put that in a welcome() function.
# Create a main program that takes in user input with input().

# Code: 
def get_item(x):
  if x == 1:
    return "🍔 Cheeseburger"
  elif x == 2:
    return "🍟 Fries"
  elif x == 3:
    return "🥤 Soda"
  elif x == 4:
    return "🍦 Ice Cream"
  elif x == 5:
    return "🍪 Cookie"

def welcome():
  print("Welcome to our restaurant! ")
  print("Here is the menu: ")
  print("1. 🍔 Cheeseburger")
  print("2. 🍟 Fries")
  print("3. 🥤 Soda")
  print("4. 🍦 Ice Cream")
  print("5. 🍪 Cookie")

welcome() 

option = int(input("What would you like to order? Pick a corresponding number: \n"))
print(get_item(option))
