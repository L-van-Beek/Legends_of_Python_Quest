# String contcatenation and string interpotation 
 
#Task: "99 Bottles of Beer" is an old song that annoying kids, oops I mean everyone, sang on road trips to pass the time.
#Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."

#Code: 
for x in range(99, 0, -1):
  print(f'{x} bottles of beer on the wall \n {x} bottles of beer \n Take one down, pass it around \n {x-1} bottles of beer on the wall')
