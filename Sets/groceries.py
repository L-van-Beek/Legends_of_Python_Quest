# Task: Fruit Cart 
# 🫐🍇🍌 Let’s go back to fruits! 🍓🍒🍎

# Grocery shopping is great until you forget what was on your list. 😥

# Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

# Create two sets representing your favorite fruits and your best friend's favorite fruits.
# Print the union of the two sets would look like.
# Print the intersection of the two sets.
# Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.

# Code: 
ljuba_groceries = {'tomatoes', 'cucumber', 'courgettes', 'chicken', 'sourdough bread', 'onions'}
dennis_groceries = {'chips', 'nuts', 'bananas', 'snacks', 'potatoes', 'tomatoes', 'chicken'}
combined = ljuba_groceries.union(dennis_groceries)
print(combined)
common_groceries = ljuba_groceries.intersection(dennis_groceries)
print(common_groceries)
unique_items = ljuba_groceries.difference(dennis_groceries)
print(unique_items)
ljuba_groceries.add('eggplants')
dennis_groceries.add('minced meat')
ljuba_groceries.remove('onions')
upd_list = ljuba_groceries.union(dennis_groceries)
print("Here is the final list: \n")
print(upd_list)
