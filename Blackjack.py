import random
from replit import clear

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

def dealcards():
  """Outputs a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card
  

def calculation(cards):
  """Calculates the score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw."
  elif computer_score == 0:
    return "Computer has blackjack, you lose. :("
  elif user_score == 0:
    return "BLACKJACK! You win. :)"
  elif user_score > 21:
    return "You exceeded 21. You lose. :("
  elif computer_score > 21:
    return "Computer exceeded 21. You win! :)"
  elif user_score > computer_score:
    return "You win! :)"
  else:
    return "You lose. :("

def playgame():
  print(logo)
  user = []
  computer = []
  gameover = False
  
  
  for x in range(2):
    user.append(dealcards())
    computer.append(dealcards())
  
  
  while not gameover:
  
    userscore = calculation(user)
    comscore = calculation(computer)
    print(f"Your cards: {user}, Current score: {userscore}")
    print(f"Computer's first card: {computer[0]}")
    
    if userscore == 0 or comscore == 0 or userscore > 21:
      gameover = True
    else:
      choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if choice == 'y':
        user.append(dealcards())
      else:
        gameover = True
    
  while comscore != 0 and comscore < 17:
    computer.append(dealcards())
    comscore = calculation(computer)
  
  print(f"Your final cards: {user}, Final score: {userscore}")
  print(f"Computer final cards: {computer}, Final score: {comscore}")
  print(compare(userscore, comscore))


while input("Do you want to play Blackjack? Type 'y' or 'n'. ") == "y":
  clear()
  playgame()
