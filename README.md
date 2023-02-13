# Computer Vision RPS
To begin the CVRPS project, a computer vision model was trained in a 'Teachable Machine'. The model trained on 4 classes (rock, paper, scissors and nothing). The rock model was trained on 763 image samples to capture images of a fist, a representation of a rock. The paper model was trained with 680 image samples to capture images of an open plan representing a paper leaf, the scissors model was trained using 800 image samples to capture a two-figured representation of a scissor and finally, a nothing model was trained on 640 image samples of no signs held against the camera.

# Milestone 2
Keras_model.h5 was created using Teachable_machines, four classes were created to capture RPS and its model data was downloaded

# Milestone 3
A new virtual environment was created 'my_env' and all dependencies along with a requirement.txt file were installed. After creating the model, testing of the model was completed and spent time understanding how the model works and what ML predictions were. RPS-Template.py was created, 

# Milestone 4
Created three functions (get_computer_choice, get_user_choice and get_winner). the first function has a list of RPS options and the module 'random' is called on it to surface a random RPS string from the RPS list. The second function gets users' input and the third and final function has the RPC game logic which decides the winner RPS in the End a new function called PLAY is created to run the game