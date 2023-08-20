#Number Guessing Game Objectives:
logo = """
                                                    )                                 
 (                            *   )    )         ( /(                   )             
 )\ )      (     (          ` )  /( ( /(    (    )\())   (      )    ( /(    (   (    
(()/(     ))\   ))\ (   (    ( )(_)))\())  ))\  ((_)\   ))\    (     )\())  ))\  )(   
 /(_))_  /((_) /((_))\  )\  (_(_())((_)\  /((_)  _((_) /((_)   )\  '((_)\  /((_)(()\  
(_)) __|(_))( (_)) ((_)((_) |_   _|| |(_)(_))   | \| |(_))(  _((_)) | |(_)(_))   ((_) 
  | (_ || || |/ -_)(_-<(_-<   | |  | ' \ / -_)  | .` || || || '  \()| '_ \/ -_) | '_| 
   \___| \_,_|\___|/__//__/   |_|  |_||_|\___|  |_|\_| \_,_||_|_|_| |_.__/\___| |_|   
                                                                                      
"""
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
def game():
  random_number = random.randint(1,100)
  print(logo)
  print("Welcom to number guessing game!")
  print("Choose a number between 1 and 100")
  difficulty_level = input("Choose difficulty level => type 'easy' or 'hard': ").strip().lower()
  chances = 0
  if difficulty_level == 'easy':
    chances = 10
  elif difficulty_level == 'hard':
    chances = 5
  else:
    print("Please choose the difficulty level again")

  exiter = False
  while chances > 0 and not exiter:
    print(f"You have {chances} attempts remaining")
    number = int(input("Enter a number: "))
    if number > random_number and number > 0 and number < 101:
      print("Too high")
      print("Guess again")
    elif number < random_number:
      print("Too low")
      print("Guess again")
    elif number == random_number:
      print("You guessed it right!")
      exiter = True
    else:
      print("choose number between 1 and 100")
      print("Guess again")
    chances -= 1
      
  if chances == 0:
    repeat = input("you lose play game again? type 'yes' to continue: ")
    if repeat == "yes":
      clear()
      game()

game()

#working with global variables

global_variable = 0

#to change the value of global variable inside th function
#use global key word
def change_global():
  global global_variable
  global_variable = 5
  #because of scoping it will create local variable which will be scoped to this function

#constants will be full capitalized
PI = 3.14

"""
python does not have the concept of block scoping
if we create any variable inside if or while or anything except functions those will have global scope by default
eg
"""

if True:
  variable_inside_if = 45

print(variable_inside_if)

#above variable_inside_if is created inside if block but that is still accessable outside the block that proves that python does not have block scope 
