import random
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a" #returns true if guess = a
  else:
    return guess == "b" #return true if guess = b


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
