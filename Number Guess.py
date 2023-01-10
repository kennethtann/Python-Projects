import random
from replit import clear


art = """
_____   __                        ______                  _________                          
___  | / /___  _____  ________ ______  /______________    __  ____/___  _____________________
__   |/ /_  / / /  / / /_  __ `__ \_  __ \  _ \_  ___/    _  / __ _  / / /  _ \_  ___/_  ___/
_  /|  / / /_/ // /_/ /_  / / / / /  /_/ /  __/  /        / /_/ / / /_/ //  __/(__  )_(__  ) 
/_/ |_/  \__,_/ \__,_/ /_/ /_/ /_//_.___/\___//_/         \____/  \__,_/ \___//____/ /____/  
                                                                                             """



def guess():
  gameover = False
  print(art)
  difficulty = input("Welcome to the NumberGuess!\nGuess a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard'. ")
  
  number = random.randint(1, 100)
  
  if difficulty == 'easy':
    x = 10
  else:
    x = 5
    
  while not gameover:
    print(f"You have {x} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == number:
      print("Awesome! You got it :)")
      gameover = True
      
    elif x == 1:
      print("You ran out of guesses.")
      print(f"The answer was {number}.")
      gameover = True
      
    elif guess > number:
      print("Too High. Guess again :(")
      x += -1
      
    elif guess < number:
      print("Too Low.\nGuess again :(")
      x += -1
    
    
while input("Do you want to play NumberGuess? Type 'y' or 'n'. ") == "y":
  clear()
  guess()
