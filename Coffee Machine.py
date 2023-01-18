MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
gameover = False
revenue = 0

def vending():
  global revenue
  global gameover
  choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
  if choice == 'latte' or choice == 'cappuccino' or choice == 'espresso':
    drink = MENU[choice]
    ingredients = drink["ingredients"]
    if resources["water"] > ingredients["water"] and resources["milk"] > ingredients["milk"] and resources["coffee"] > ingredients["coffee"]:
      cash = float(input("Insert cash: $"))
      revenue += cash
      while cash < drink["cost"]:
        short = drink["cost"] - cash
        choice2 = input(f"Sorry, you are short of ${short}. Type 'y' to insert more cash or 'n' to refund.").lower()
        if choice2 == 'y':
          choice3 = float(input("Insert cash: $"))
          cash += choice3
          revenue += choice3
        else:
          print(f"${cash} refunded.")
          revenue -= cash
          gameover = True
      if cash > drink["cost"]:
        change = cash - drink["cost"]
        revenue -= change
        print(f"Here's your change. ${change}")
      print(f"Enjoy your {choice}. Have a nice day!")
      resources["water"] -= ingredients["water"]
      resources["milk"] -= ingredients["milk"]
      resources["coffee"] -= ingredients["coffee"]
    else:
      print("Sorry, not enough ingredients :(")
      choice4 = input("Would you like to order something else? 'Type 'y' or 'n'. ").lower()
      if choice4 == 'n':
        gameover = True
      
  elif choice == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Revenue: ${revenue}")
  elif choice == 'off':
    print("Machine will shutdown.")
    gameover = True

while not gameover:
  vending()

