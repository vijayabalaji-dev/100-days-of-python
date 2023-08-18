import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


user_cards = [deal_card(),deal_card()]
computer_cards = [deal_card(),deal_card()]

def calculate_score(list,type):
  if sum(list) == 21 and len(list) == 2:
    return 0
  if 11 in list and sum(list) > 21 and type == "user":
    user_cards.remove(11)
    user_cards.append(1)
  return sum(list)


print(logo)
print(f"your card {user_cards}")
print(f"computer first card {computer_cards[0]}")

def evaluate(user,computer):
  if user == 0 or computer == 0:
      print("you lose")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif user < 21 and computer < 21:
    return False
  elif user == 21:
      print("you win")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif computer > 20:
      print("you lose")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif user > computer and user < 21:
     print("you win")
     print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif user == 21 and computer == 21:
      print("draw")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif user > computer and user < 21:
      print("you win")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif user > computer and user > 21:
    print("you lose")
    print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
  elif computer > user:
      print("you lose")
      print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")

exiter = False
while not exiter:
  inp = input("'y' to append 'n' to pass?: ").strip()
  if inp == 'n':
    user = calculate_score(user_cards,"user")
    computer = calculate_score(computer_cards,"computer")
    res = evaluate(user,computer)
    if res == False:
      if user > computer:
        print("you Win")
        print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
      else:
        print("you lose")
        print(f"yours {user_cards} = {user} and computer {computer_cards} = {computer}")
    exiter = True
  if inp == 'y':
    user = calculate_score(user_cards,"user")
    computer = calculate_score(computer_cards,"computer")
    user_cards.append(deal_card())
    user = calculate_score(user_cards,"user")
    res = evaluate(user,computer)
    if res == False:
      print(f"yours {user_cards} and computer {computer_cards[0]}")
      continue
    else:
      exiter = True

