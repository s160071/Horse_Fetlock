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
7) PictureNormalization.ipynb
8) Architecures_test.ipynb
9) Evaluate_final_model.ipynb


# 1) MISSING (MAKE X,Y COORDS)
This script was used to open and show 1100x650 sized images, whereas the user could manually click the center of the knee across all the pictures which would be stored for training the future localization network.

# 2) Data_augmentation_v2.ipynb
This script was used to augment the data, since the originally only 134~ pictures exsists. The script augments the data by mirroring the picture, rotating the picture 180 degrees and finally a combination of the two. This script also translates the X,Y coordinates to the augmented data, to avoid having to manually click the center of the knees.

# 3) Localizer_v2.ipynb
This script includes the architecture and training/validation of the localization network created using Pytorch. The network was trained on the original and augmented X, Y coordinates mentioned above.

# 4) Save_Cropped_Output_Snipped.ipynb
Due to the exam presentation, and overall validating that the localization network made correct X,Y predictions all the images was created to PNG files and inspected. Ideally the end result would have the localization network followed by the classification network. But having only the output from the localization network, made the rest of the research much faster.

# 5) Rotate_Data_And_Pickle.ipynb
As mentioned at the exam presentation, the first data augmentation was just a "simple" augmentation. And we had already planned to augment the data further by rotating the images. This script includes the code to rotate the output from the localization network. And introduces labels when saving the picture describing whether the image is original, augmented via mirror/180 rotation or rotated. Which makes simplifies future use.

# 6) NoAugmentation_Keras_Classifer_New_Trainingset.ipynb
Having tested No-Augmentation, Augmentation via mirror/180 rotation, and Augmentation via small steps of rotation and finding out that the dataset with no augmentation did best in test. The NoAugmentation dataset was saved for future use. Additionally the training/testing for this specific (No augmentation) can also be found in the script.

# 7) PictureNormalization.ipynb
This script includes the various image normalization techniques, including the AHE method.

# 8) Architecures_test.ipynb
This script includes the intialization of all the network architectures used in configuration 4 from the report. Including the final model.

# 9) Evaluate_final_model.ipynb
This script includes the loading of all the 10 initializations for the final architecture used "Dilation v1 (F)". Of these 10 intializations the very best of these versions are used to evaluate across the testing set. Which resulted in an accuracy of ~88.25%, additionally the images of the misclassifications are viewed.
