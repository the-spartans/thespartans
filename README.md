# the-spartans
plant disease detection module

This module is designed to differentiate between a diseased plant and a healthy plant based on its leaf size and colour parameters.

DATASET
Here the database selected is for the case of tomato plants affected by viral disease. A dataset of 43 samples has been created for a supervised learning module with 2 labels and 3 parameters.
The two labels are the general classification of 'healthy', 'unhealthy' and the further classification of the stages of viral infection as 'stage-I', 'stage-II' and 'stage-III'.
The parameters considered are length of the leaf, width of the leaf and the hue factor of the processed image. 
The ideal length of the leaf has been taken as the average length taken over a number of samples, and the width as the width observed at the centre of the leaf and taken as the average width taken over a number of samples. 
The image of the plants have been obtained and processed under various filters and the hue value for a diseased plant and for an unaffected plant has been taken for consideration.

ALGORITHM
This module implements supervised learning of machine learning.
The basic packages like numpy, matplotlib, pandas, sklearn are installed and imported from python.
Using file handling methods in python a csv file is created and the dataset data is entered and stored in the file.
Import the dataset using the pandas package and call the classifier function. This is to clasify the data in the data set into a tree like structure.
To train the algorithm pass all the parameters and the labels as the training set using the train function.
Specify the label of the dataset given as the dataset
To provide the test set enter the parameters of the dataset without the classification labels.
Then the output is predicted using the predict function and the output is printed.
