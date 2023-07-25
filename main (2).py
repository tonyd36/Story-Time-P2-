#Title
from typing import cast

print("- Enchanted Lands of UMBC -")

print()

#Introduction
print("You are a knight in the year 650 CE sent into the enchanted lands of UMBC.")

print()
print()

# Introduction Part 2 
print("Your training leads you to Hilltop castle to find an item.")

option_1 = ("A")
option_2 = ("B")
option_3 = ("C")

#Scenario 1, Choosing which path to go down. The user is given the choice of the blacksmith, town's teacher, and the king

print("You arrive at the castle and notice three people need help.")
print("However, you can only choose one because you must return home.")
print("You could speak to: ")
print("A. The local blacksmith looking for a legendary sword")
print("B. The town's teacher who needs assisstance")
print("C. The king, who needs a warrior")
castle_ground = input("Please enter option A-C: ")

print()
print()

#Choice A: Blacksmith scenario which will take the user down the path to find the sword
choice_1 = ("A")
choice_2 = ("B")
choice_3 = ("C")

#Statement that takes the user to question for the sword. 
if castle_ground == option_1 :
  print("You meet with the town's blacksmith, looking for the sword")
  print("The blacksmith says the sword is said to be in the Jungle of Baltimore")
  print("He bids you farewell, and you choose to search: ")
  print("A. The Arbutus Artic")
  print("B. The Baltimore Jungle")
  print("C. The Pasadena Desert")
  store = input("Please enter option A-C: ")

#Runs if the user selects B as the correct answer where they have completed the story
  if store == choice_2 :
      print("Congrats! you found the sword and as a gift the blacksmith forges axes!")
      print("You return to your lands as a true hero")
    
#If the user chooses the wrong biome then then they have failed and are meant to try again
  else:
      print("Pay closer attention next time. As a result you perished in the chosen biome")
  
print()
print()

#Part 2 which if selected will take the user to the town's teacher where they have to answer a math question
solution_1 = 20
if castle_ground == option_2 :
  print("The town teacher needs your help with a basic math problem.")
  print("The admit they aren't qualified to teach and need help.")
  print("x = (6 * 3) + 2")
  solution = int(input("Please enter the solution: "))

#The correct answer is 20 and if the user inputs the correct answer then they have succeeeded and completed the story
  if solution_1 == solution :
    print("'Thank you!' the teacher cries, and you receive an honorary degree")
    print("You return to your land with a degree and a new sense of pride.")

#If the user inputs the wrong answer then the program will show this print statement
  else:
    print("'Ummmm... I know that is incorrect. Please take a seat with the students")
    print("You are stuck in the classroom for the next 8 years")
    print("THE END")   

print()
print()

#Part 3 of the story will take the user to the King where they are tasked with answering another math question to receieve a magic tusk 
x = 6
y = 4
z = 10
z = x + y

#This statement explains the situation and the question they are meant to answer in order to complete the story
if castle_ground == option_3 :
  print("You meet with the king who tells you to hunt with him.")
  print("You and him ride off into the forest to find a rare boar")
  print()
  print("The rare boar says, 'I will give you a magic tusk if you can solve this.'")
  print("Give me 2 numbers that add up to 10")
  print()
  print("After pondering you decide on two numbers... ")
  answer_1 = int(input("Please enter 1st number: "))
  answer_2 = int(input("Please enter 2nd number: "))
  sum = answer_1 + answer_2

#This code will run if the user inputs the correct values to add up to 10
  if sum == 10 :
    print(f"Correct! {answer_1} and {answer_2} add up to 10")
    print("I give you my left tusk giving you luck and strength!")
    print("THE END")
#This code will run if the user inputs the wrong values
  else:
    print("Sorry that is incorrect come back in 50 years to try again")
