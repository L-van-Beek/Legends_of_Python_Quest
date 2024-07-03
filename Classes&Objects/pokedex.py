# Task: 
# Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters. A Pokédex is a device that tracks the information for Pokémon that are seen or caught.

# Create a new file called pokedex.py.

# Next, let's define a Pokemon class with the following attributes:

# - entry (integer)
# - name (string)
# - types (list of strings)
# - description (string)
# - is_caught (boolean)
# Note: Make sure to use the __init__() method.
# Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!
# Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

# - Entry Number: 25
# - Name: Pikachu
# - Type: Electric
# - Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
# - Pikachu has already been caught!

# Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

# Code: 
class Pokemon:
  def __init__ (self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types 
    self.description = description 
    self.is_caught = is_caught 

  def speak(self):
    print(self.name * 2)

  def display_details(self):
    print("Entry number:" + str(self.entry)) 
    print("Name:" + str(self.name))
    print("Type:" + str(self.types))
    print("Description:" +str(self.description))
    if self.is_caught == True:
      print(self.name + " has already been caught")
    else:
      print(self.name + " has not yet been caught")

pikachu = Pokemon(1, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
charmander = Pokemon(2, "Charmander", "Fire", "The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.", False)
jigglypuff = Pokemon(3, "JigglyPuff", "Normal, Fairy", "When its huge eyes waver, it sings a mysteriously soothing melody that lulls its enemies to sleep.", True)

pikachu.speak()
pikachu.display_details() 

charmander.speak()
charmander.display_details() 

jigglypuff.speak()
jigglypuff.display_details() 


