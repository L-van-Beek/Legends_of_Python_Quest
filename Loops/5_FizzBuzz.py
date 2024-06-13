#Task: Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝
#Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively. Want to give it a try?
#Create a fizz_buzz.py program that outputs numbers from 1 to 100.
# Here's the catch:
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

#Code: 
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)


#Another exercise I tried to accomplish myself with multiples of 3 being replaced by "Ding" and multiples of 2 being replaced with "Dong". Range is 1 to 50.


#Code: 
for x in range(1, 51):
  if x % 3 == 0:
    print("Ding")
  elif x % 2 == 0:
    print("Dong")
  else:
    print(x)
