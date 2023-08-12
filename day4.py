#askpythom.com
#to learn more about python modules

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

num = random.randint(0,1)

if num == 0:
    print("Tails")
else:
    print("Heads")

#tresure hunt
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

str_pos = str(position)
d1 = int(str_pos[0])
d2 = int(str_pos[1])
map[d2 -1][d1 -1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


#rock paper scissor
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
user_choice = input("Enter 0 for rock, 1 for paper and 2 for scissor ? ")
random = random.randint(0,2)
if int(user_choice) == 0:
  print("you choose rock")
  print(rock)
  if random == 0:
    print("computer chooses rock")
    print(rock)
    print("it is a tie")
  elif random == 1:
    print("computer chooses paper")
    print(paper)
    print("you lose")
  else:
    print("computer chooses scissor")
    print(scissors)
    print("you win")
elif int(user_choice) == 1:
  print("you choose paper")
  print(rock)
  if random == 0:
    print("computer chooses rock")
    print(rock)
    print("you win")
  elif random == 1:
    print("computer chooses paper")
    print(paper)
    print("it a tie")
  else:
    print("computer chooses scissor")
    print(scissors)
    print("you lose")
else:
  print("you choose scissor")
  print(rock)
  if random == 0:
    print("computer chooses rock")
    print(rock)
    print("you lose")
  elif random == 1:
    print("computer chooses paper")
    print(paper)
    print("you win")
  else:
    print("computer chooses scissor")
    print(scissors)
    print("it's a tie")
    
    
    
