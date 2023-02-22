import random
import cv2
import time
from keras.models import load_model
import numpy as np

class RPS():
    def __init__(self, rounds_played=0, computer_wins=0, user_wins=0):
        self.rps = ['Rock', 'Paper', 'Scissors']
        self.model = load_model('keras_model.h5')
        self.rounds_played = rounds_played
        self.computer_wins = computer_wins
        self.user_wins = user_wins

    def get_computer_choice(self):
        choice = random.choice(self.rps)
        return choice

    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = self.model.predict(data)
            cv2.imshow('frame', frame)
        # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            max_predict = np.max(prediction)
            max_index = np.where(prediction == np.max(prediction))
            prediction_index = max_index[1][0]
    # After the loop release the cap object
        cap.release()
    # Destroy all the windows
        cv2.destroyAllWindows()
        print(prediction_index)
        return prediction_index

    def get_winner(self):
        computer = self.get_computer_choice()
        user = self.get_prediction()
        if computer == self:
            print('It is a tie!')
        elif computer == 'Rock' and user == 1:
            self.user_wins += 1
            #self.computer_wins -= 1
            print('You won!')
        elif computer == 'Paper' and user == 2:
            self.user_wins += 1
            #self.computer_wins -= 1
            print('You won!')
        elif computer == 'Scissors' and user == 0:
            self.user_wins += 1
            #self.computer_wins -= 1
            print('You won!')
        else:
            self.computer_wins += 1
            #self.user_wins -= 1
            print('You lost')
        self.rounds_played += 1

    def play_game(self, rounds_played=0):
        while True:
            if self.user_wins == 3:
                break
            elif self.computer_wins == 3:
                break
            elif self.rounds_played == 5:
                break

a = RPS()
a.get_winner()
print(a.computer_wins)
print(a.user_wins)
print(a.rounds_played)