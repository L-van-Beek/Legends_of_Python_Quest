# Task: In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:

# 'Bob\'s Burgers'
# 'American Diner'
# 4.7
# False
# Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.
# Then, use print(vars()) to output each of the three restaurants!

# Code: 
class Restaurant:
  name = ""
  category = ""
  raiting = 0.0
  delivery = False 
bobs_burgers = Restaurant()
bobs_burgers.name = "Bob\'s burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.raiting = 4.7
bobs_burgers.delivery = False 
mia_casa = Restaurant()
mia_casa.name = "Mia Casa"
mia_casa.category = "Italian"
mia_casa.raiting = 4.8 
mia_casa.delivery = True 
lune = Restaurant()
lune.name = "Lune"
lune.category = "French bakery"
lune.raiting = 5.0
lune.delivery = False 
print(vars(bobs_burgers))
print(vars(mia_casa))
print(vars(lune))
