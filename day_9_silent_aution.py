from replit import clear
#from art import logo
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


auction_dict = {}
exit = False
print(logo)
print("Welcome to the secret auction program ...")
while not exit:
  name = input("what is your name?: ").strip().lower()
  amt = int(input("What is your bid?: "))
  ask = input("'yes' to continue biding , 'no' to stop biding?: ").lower().strip()
  auction_dict[name] = amt 
  if ask == "yes":
    clear()
    continue
  else:
    if auction_dict:
      max_bidder = list(auction_dict.keys())[list(auction_dict.values()).index(max(list(auction_dict.values())))]
      clear()
      print(f"The winner is {max_bidder} with the bid of ${auction_dict[max_bidder]}.")
    exit = True
