# Task: Countdown

# Let's use the datetime and random modules to make a birthday card to determine how far your birthday is from today! 🎂
# For this exercise, we are creating two .py files in a separate code editor.

import random 
bday_messages = ["Hope you have a very Happy Birthday! 🎈", "It's your special day – get out there and celebrate! 🎉", "You were born and the world got better – everybody wins! 🥳", "Have lots of fun on your special day! 🎂", "Another year of you going around the sun! 🌞"]
random_message = random.choice(bday_messages)
print(random_message)
