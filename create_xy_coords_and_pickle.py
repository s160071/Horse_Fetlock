# import the necessary packages
import cv2
import os
import numpy as np
import glob
import matplotlib.pyplot as plt
import pickle

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not

def click_and_crop(event, x, y, flags, param):
    # (x, y) coordinates and indicate that cropping is being
    # performed
    global refPt_end, refPt_start
    global zoom
    global x_pos, y_pos

    if event == cv2.EVENT_LBUTTONDOWN:
        zoom = 21
        refPt_start = (x-zoom, y-zoom)
        refPt_end = (x+zoom, y+zoom)
        x_pos = x
        y_pos = y

        cv2.rectangle(image, refPt_start, refPt_end, (0, 255, 0), 2)
        cv2.imshow("image", image)


big_picture_array = []
big_dir = r"G:\Deep_Learning_Horse\Data_Sorted\Splinter\Uniform_big"
small_dir = r"G:\Deep_Learning_Horse\Data_Sorted\Splinter\Uniform_small"

os.chdir(small_dir)

for picture_name in glob.glob("*.png"):
    print(picture_name)
    image = cv2.imread(picture_name)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            # Get X, Y of click.
            # Get big picture [0]
            # Get small picture [1]
            # Get X, Y position [2]
            # Get Healthy/Spliter label [3]
            # Combine them into 1 array and pickle

            os.chdir(big_dir)
            big_picture_name = "resize" + picture_name[12:] + ".png"
            big_picture = plt.imread(big_picture_name)

            os.chdir(small_dir)
            small_picture = plt.imread(picture_name)

            x_y = np.array((x_pos, y_pos))

            big_picture_array.append([big_picture, small_picture, x_y, 1])


            cv2.destroyAllWindows()
            #image = np.array(image)
            #crop_img = clone[refPt_start[1]:refPt_end[1], refPt_start[0]:refPt_end[0]]
            #cv2.imwrite(picture_name[:-4] + "s" + str(refPt_start) + "e" + str(refPt_end) + ".png", crop_img)
            #cv2.imshow("cropped", crop_img)
            break

    cv2.destroyAllWindows()
# close all open windows

cv2.destroyAllWindows()

big_picture_array = np.array(big_picture_array)
print(big_picture_array.shape)

with open('splinter_array.pickle', 'wb') as handle:
    pickle.dump(big_picture_array, handle, protocol=pickle.HIGHEST_PROTOCOL)