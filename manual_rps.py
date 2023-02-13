import random

def get_computer_choice():
    rpc = ['rock', 'paper', "scissors"]
    choice = random.choice(rpc)
    return choice

def get_user_choice():
  item = input("Input: ")
  return item
