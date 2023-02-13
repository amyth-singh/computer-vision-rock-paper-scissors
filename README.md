# Computer Vision RPS
To begin the CVRPS project, a computer vision model was trained in 'Teachable Machine'. The model trained on 4 classes (rock, paper, scissors and nothing). The rock model was trained on 763 image samples to capture images of a fist, a representation of a rock. The paper model was trained with 680 image samples to capture images of an open plam representing a paper leaf, the scissors model was trained using 800 image samples to capture a two fingured representation of a scissor and finally a nothing model was trained on 640 image samples of no signs held against the camera.

# Milestone 4
Created three functions (get_computer_choice, get_user_choice and get_winner). the first function has a list of rpc options and the module 'random' is called on it to surface a random rpc string from the rpc list. The second function gets a users input and the third and final function has the RPC game logic which decides the winner and in the end a new function called PLAY is created to run the game