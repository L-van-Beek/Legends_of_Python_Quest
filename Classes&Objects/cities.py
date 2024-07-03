# Task: 
# Ever wonder how many people live in New York City? What about London?

# Create a favorite_cities.py program.

# Let's make a City class that uses the __init__() method to define the following attributes:

# name (string)
# country (string)
# population (integer rounded to the nearest thousand people)
# landmarks (list of strings)
# Next, create an object for your hometown and assign the attributes above.

# Lastly, create another object of the city that you've always wanted to visit!
# Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.

# Code: 

class City:
  def __init__ (self, name, population, landmarks, founding_year, mayor):
    self.name = name 
    self.population = population
    self.landmarks = landmarks
    self.founding_year = founding_year
    self.mayor = mayor 
new_york = City("New York", 8300000, "Brooklin Bridge, Empire State Building, Statue of Liberty", 1624, "Eric Adams")
london = City("London", 9000000, "Tower of London, Buckingham Palace, Tower Bridge", "47 AD", "Sadiq Khan")
amsterdam = City("Amsterdam", 822000, "Amsterdam Centraal, Rijksmuseum, Royal Palace Amsterdam", 1275, "Femke Halsema")
print(vars(new_york))
print(vars(london))
print(vars(amsterdam))
