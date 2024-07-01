List Method	& Description
.append()	Add an item to the end of the list
.clear()	Remove all items from the list
.copy()	Return a shallow copy of the list
.count()	Return the number of times the value appears in the list
.extend()	Appends another list to the current list by extending it
.index()	Returns the index of a value inside the list
.insert()	Insert an item at a specified position in the list
.pop()	Remove an item from a specified position in the list
.remove()	Remove an item from the list based on the value of the item
.reverse()	Reverses the list in place
.sort()	Sorts the list in place

# Task: 
# Let's start a book club by making a list of tech startup books! 📚

# Create a reading_list.py program that stores the following items in a books list:

# 'Zero to One'
# 'The Lean Startup'
# 'The Mom Test'
# 'Make It Stick'
# 'Life in Code'
# A. Suppose we want to add one more book to the list: 'Zero to Sold'. Can you use a list method to do so?
# B. Let's say we finished reading 'Zero to One' and 'The Lean Startup'. 
# C. Print the updated list out to make sure everything's good to go!

# Code: 
reading_list = ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code']
reading_list.insert(5, 'Zero to Sold') 
print(reading_list) #A. 
reading_list.remove('Zero to One')
reading_list.pop(0)
print(reading_list) #B. 
