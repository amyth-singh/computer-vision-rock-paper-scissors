import random

def get_computer_choice():
    rpc = ['rock', 'paper', "scissors"]
    choice = random.choice(rpc)
    return choice

def get_user_choice():
  item = input("Input: ")
  return item

def get_winner(computer_choice, user_choice):
  computer_choice = get_computer_choice()
  if (computer_choice == user_choice):
    print("It is a tie!")
  elif (computer_choice == "rock") and (user_choice == "paper"):
    print("You won!")
  elif (computer_choice == "scissors") and (user_choice == "rock"):
    print("You won!")
  elif (computer_choice == "paper") and (user_choice == "scissors"):
    print("You won!")
  else:
    print("you lost")

get_winner("rock", "paper")