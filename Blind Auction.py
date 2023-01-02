from replit import clear

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

bids = {}

def bid(person, price):
  bids[person] = price
  

option = 'yes'
while option == 'yes':
  print(logo)
  name = input("What is your name? ")
  offer = int(input("What is your offer? $"))
  
  bid(person=name, price=offer)

  option = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  
highest = 0
winner = ""
for bidder in bids:
  if bids[bidder] > highest:
    highest = bids[bidder]
    winner = bidder

print(f"The winner is {winner} with a bid of ${highest}.")
  
