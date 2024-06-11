# Assignment "Sorting Hat"  💖

Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0
print("------------------------------------")
print("Welcome to the sorting Hat ceremony!")
print("------------------------------------")

print("Before the Hat decides to which house you belong, you need to answer some questions:")
print("----------")
print("Question 1")
print("----------")
answer1 = int(input("Do you like Dawn or Dask? \n 1. Dawn \n 2. Dusk \n Type the corresponding number (1 or 2): "))
if answer1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")
print("----------")
print("Question 2")
print("----------")
answer2 = int(input("When I'm dead, I want people to remember me as: \n 1. The Good \n 2. The Great \n 3. The Wise \n 4. The Bold \n Type the number: "))
if answer2 == 1:
  Hufflepuff += 2
elif answer2 == 2:
  Slytherin += 2
elif answer2 == 3:
  Ravenclaw += 3
elif answer2 == 4:
  Gryffindor += 2
else:
  print("Wrong input")
print("----------")
print("Question 3")
print("----------")
answer3 = int(input("Which kind of instrument most pleases your ear? \n 1. The violin \n 2. The trumpet \n 3. The piano \n 4. The drum \n Type the number: "))
if answer3 == 1:
  Slytherin += 4
elif answer3 == 2:
  Hufflepuff += 4
elif answer3 == 3:
  Ravenclaw += 4
elif answer3 == 4:
  Gryffindor += 4
else:
  print("Wrong input")
print("Now it is time to see your house!")
max_points = max(Gryffindor, Slytherin, Hufflepuff, Ravenclaw)
if Gryffindor == max_points:
  print("Welcome to Gryffindor!")
elif Slytherin == max_points:
  print("Welcome to Slytherin!")
elif Hufflepuff == max_points:
  print("Welcome to Hufflepuff!")
elif Ravenclaw == max_points:
  print("Welcome to Ravenclaw!")
