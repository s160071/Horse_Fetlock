# Horse_Fetlock
Deep Learning 02456 course project

Sequence the files should be run:
0) RESHAPING THE PICTURES (ANDREAS)
1) MISSING (MAKE X,Y COORDS)
2) Data_augmentation_v2.ipynb
3) Localizer_v2.ipynb
4) Save_Cropped_Output_Snipped.ipynb
5) Rotate_Data_And_Pickle.ipynb
6) NoAugmentation_Keras_Classifer_New_Trainingset.ipynb
7) Architecures_test.ipynb
8) Evaluate_final_model.ipynb


# 1) MISSING (MAKE X,Y COORDS)
This script was used to open and show 1100x650 sized images, whereas the user could manually click the center of the knee across all the pictures which would be stored for training the future localization network.

# 2) Data_augmentation_v2.ipynb
This script was used to augment the data, since the originally only 134~ pictures exsists. The script augments the data by mirroring the picture, rotating the picture 180 degrees and finally a combination of the two. This script also translates the X,Y coordinates to the augmented data, to avoid having to manually click the center of the knees.

# 3) Localizer_v2.ipynb
