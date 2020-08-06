import numpy as np
import cv2
import os
import pathlib

def resize_pic(folder_path, output_path, resized):
   #print(folder_path)
    files = os.listdir(folder_path)
    l = len(files)
    #print("l:", l)
    if (resized == 0):
        for i, img in zip(range(l), files):
            #print(i, img)
            name = folder_path + str(i) + ".png"
            name2 = output_path + str(i) + ".png"
            print("output : ", name2)
            #name = folder_path + img
            file_loc = pathlib.Path(name)
            if file_loc.exists():       # check ls -a to check if there are some hidden files and remove it
                print("File exist")
                print("name :", name)
                # Reading the image in RGB mode
                image = cv2.imread(name)
                print(image.shape)
                # Resize Image to original VGG16 input size
                # from the paper: "During training, the input to our ConvNets
                # is a fixed-size 224 × 224 RGB image"
                width = 224
                height = 224
                dim = (width, height)
                # resize image
                resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
                cv2.imwrite(name2, resized_image)
                #cv2.imshow("Res", image)
                #cv2.waitKey(0)

            else:
                print("File not exist")
                print("name :", name)


    else:
        print("Already Renamed")


def rename_folder_images(folder_path, renamed):
    # Bash command to rename space to underscore - run in terminal -> for f in *\ *; do mv "$f" "${f// /_}"; done
    print(folder_path)
    files = os.listdir(folder_path)
    if(renamed == 0):
        for index, file in enumerate(files):
            os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.png'])))
    else:
        print("Already Renamed")

path = 'Dataset/Others/'
output = 'Dataset/Others_re/'
rename_folder_images(path, 0) # 0 = rename, 1 = not to rename
resize_pic(path, output, 0) # 0 = resize, 1 = not to resize
