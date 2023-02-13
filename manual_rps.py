import random

rpc = ['rock', 'paper', "scissors"]

def get_computer_choice():
    choice = random.choice(rpc)
    return choice

def get_user_choice():
  item = input("Input: ")
  return item
