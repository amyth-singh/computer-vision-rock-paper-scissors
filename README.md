# Computer Vision RPS
To begin the CVRPS project, a computer vision model was trained in a 'Teachable Machine'. The model trained on 4 classes (rock, paper, scissors and nothing). The rock model was trained on 763 image samples to capture images of a fist, a representation of a rock. The paper model was trained with 680 image samples to capture images of an open plan representing a paper leaf, the scissors model was trained using 800 image samples to capture a two-figured representation of a scissor and finally, a nothing model was trained on 640 image samples of no signs held against the camera.

# 
Keras_model.h5 was created using Teachable_machines, four classes were created to capture RPS and its model data was downloaded, the entire experience was documented above CVRPS# 

# 
A new virtual environment was created 'my_env' and all dependencies along with a requirement.txt file were installed. After creating the model, testing of the model was completed and spent time understanding how the model works and what ML predictions were. RPS-Template.py was created, 

# 
Created three functions (get_computer_choice, get_user_choice and get_winner). the first function has a list of RPS options and the module 'random' is called on it to surface a random RPS string from the RPS list. The second function gets users' input and the third and final function has the RPC game logic which decides the winner RPS in the End a new function called PLAY is created to run the game

# 
In this milestone the hard-coded user guess with the output gets replaced by the computer vision model in the camrera_rps.py file. A new function called get_prediction() is created that returns the output of the model, the max prediction and the index of the prediction. The user plays using the camera against computers random choice and a series of condtions are written to get the winner and create round conditions. All of these have been nested within a class to make the code clearner and DRY. 

<img src="C:\Users\amith\Desktop\Ai-Core\computer-vision-rock-paper-scissors\cam_rps.png" alt="Camerarps" />
