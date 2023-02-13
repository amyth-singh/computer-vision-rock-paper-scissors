import random

def get_computer_choice():
    rpc = ['Rock', 'Paper', 'Scissors']
    choice = random.choice(rpc)
    return choice

def get_user_choice():
  item = input("Input: ")
  return item

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print('It is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        print('You won!')
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print('You won!')
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print('You won!')
    else:
        print('You lost')