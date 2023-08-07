#advanced BMI calculator
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)

if bmi <= 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi > 25 and bmi <=30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi > 30 and bmi <=35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")

#another implementation
if bmi <= 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi <=30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi <=35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
#the above implementation ius right because only if if statement fails it will go to next elif if that elif also files it will go to next elif and so on if none of the if block got executed else block will be executed


#Find leap year or not
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#rollar coster
print("Welcome to rollar coster")
height = int(input("Enter your height? \n"))
if height > 120:
    age = int(input("Enter your age ? \n"))
    if age < 12:
        amt = 5
    elif age <= 18:
        amt = 7
    else:
        amt = 12
    photo = input("do you want photo? type yes or no ")
    if photo.lower() == "yes":
        amt += 3
        print(f"your total bill is {amt}")
    else:
        print(f"your total bill is {amt}")
    
else:
    print("you have to grow....")


#pizza order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amt = 0
if size == "S":
    amt = 15
elif size == "M":
    amt = 20
elif size == "L":
    amt = 25

if add_pepperoni == "Y":
    if size == "S":
        amt += 2
    else:
        amt += 3

if extra_cheese == "Y":
    amt += 1

print(f"Your final bill is: ${amt}.")


##love calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1+name2).lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

true = str(t+r+u+e)
love = str(l+o+v+e)

true_love = int(true+love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")


#treasure hunt
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first = input("You are on your way choose lest or right? ")
if first.lower() == "left":
  second = input("you arrived at the point swim ot wait for boat ? ")
  if second.lower() == "boat":
    third = input("arrived at final destination choose door to open red, yellow or blue")
    if third.lower() == "red":
      print("Burned by fire.Game Over.")
    elif third.lower() == "blue":
      print("Eaten by beasts.Game Over.")
    elif third.lower() == "yellow":
      print("You Win!")
    else:
      print("Game Over")
  else:
    print("Game Over.")
else:
  print("Fall into a hole.Game Over.")
