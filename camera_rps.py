import random
import cv2
import time
from keras.models import load_model
import numpy as np

# Press q to close the window

def get_computer_choice(): # computer makes a random prediction
    rpc = ['Rock', 'Paper', 'Scissors']
    choice = random.choice(rpc)
    return choice

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
    # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        max_predict = np.max(prediction)        
# After the loop release the cap object
    cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()

computer_wins = [] # captures no of computer wins
user_wins = [] # captures no of user wins
rounds_played = []

def get_winner(): #creates win logic
    computer_choice = get_computer_choice()
    user_choice = get_prediction()

    if computer_choice == user_choice:
        print('It is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        user_wins.append('Win')
        computer_wins.append('Lose')
        print('You won!')
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        user_wins.append('Win')
        computer_wins.append('Lose')
        print('You won!')
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        user_wins.append('Win')
        computer_wins.append('Lose')
        print('You won!')
    else:
        user_wins.append('Lose')
        computer_wins.append('Win')
        print('You lost')

def counter(): # creates a game counter
  start = time.time()
  wait = time.time() + 1
  while time.time() < wait:
    print(wait)
  print("Chose Rock!")

def winner_check():
    if len(computer_wins) == 3:
        print("Computer Wins!")
    elif len(user_wins) == 3:
        print("User Wins!")
    elif len(rounds_played) == 5:
        print("Game Over!")
    else:
        print("End")

get_prediction()
get_winner()
counter()
winner_check()
print(get_computer_choice())
print(computer_wins)
print(user_wins)