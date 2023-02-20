
import cv2
import time
from keras.models import load_model
import numpy as np

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
    # After the loop release the cap object
    cap.release()
    # # Destroy all the windows
    cv2.destroyAllWindows()
    # prints the maximum value from a list of predictions
    max_predict = np.max(prediction)
    print(max_predict)

# calles the get-prediction model
get_prediction()

# creates a count down timer for one second
start_time  = time.time()
while time.time() < start_time + 1:
    print(start_time)
print("you chose rock")

computer_wins = []
user_wins = []

while True:
    if (len(computer_wins) == 3) or (len(user_wins) == 3) or (len(rounds_played) == 5):
        print(get_prediction())

