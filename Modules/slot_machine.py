# Create a slot_machine.py program using random.

# The items are symbols of common fruits and sevens (7️⃣). 
# In each round, the slot machine displays three random items. If there are three sevens, you win!
# Create a symbols list and include the following items: '🍒',' 🍇', '🍉', '7️⃣'.
# Next, create a results variable that uses the .choices() method from the random module and get three random symbols. 
# Then, print each value from results, separated by | pipe characters: 🍉 | 🍒 | 🍇
# Lastly, use an if/else statement:

# - If all of the list items in results are equal to '7️⃣', print "Jackpot! 💰".
# - Else, print "Thanks for playing!".
# - Rewrite this program with a play() function.
# - Add a while loop for the player to keep playing, round after round.
# - Ask the player for a 'Y' or 'N' input to keep playing with input().
# Code: 

import random 
symbols = ['🍒', '🍇', '🍉', '7️⃣']
def play(): 
  for i in range(1):    
    results = random.choices(symbols, k=3)
    print(f'{results[0]} | {results[1]} | {results[2]}')
    win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if win:
      print('Jackpot!!! 💰')
      break
    else:
      results = random.choices(symbols, k=3)

answer = ''
while answer.upper() != '0':
  play()
  answer = input('Press "7" to try again, and "0" to end the game: ')

print('Thanks for playing!')
