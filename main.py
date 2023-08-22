from game_data import data
import random
from replit import clear
from art import logo,vs
def return_random():
  """returns the random data"""
  random_data = random.choice(data)
  return [f"{random_data['name']} ,a {random_data['description']} ,from {random_data['country']}",random_data['follower_count']]

exiter = False
total = 0
while not exiter:
  print(logo)
  print(f"Your current score {total}\n\n")
  input1 = return_random()
  count1 = input1[1]
  input2 = return_random()
  count2 = input2[1]
  print(f"Option A: {input1[0]}")
  print(vs)
  print(f"Option B: {input2[0]}")
  user = input("Who has more followers? Type 'A' or 'B':").strip()
  if user == "A" and count1 > count2:
    total += 1
    clear()
  elif user == "B" and count2 > count1:
    total += 1
    input1 = input2
    count1 = count2
    clear()
  elif count1 == count2:
    print("Its a draw")
    total += 1
  else:
    clear()
    print(logo)
    print(f"Sorry that is wrong, total is {total}")
    exiter = True