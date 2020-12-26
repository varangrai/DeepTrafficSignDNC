"""
Converting German Traffic Signs dataset in YOLO format
"""
# Converting annotations written in csv file into YOLO format
#
# Algorithm:
# Setting up full path --> Lists for categories -->
# --> Loading dataFrame with original annotations -->
# --> Calculating numbers for YOLO format without normalization -->
# --> Getting image's real width and height -->
# --> Normalizing numbers for YOLO format -->
# --> Saving annotations in txt files -->
# --> Saving images in jpg format
#
# Result:
# txt files next to every image with annotations in YOLO format


# Importing needed libraries
import pandas as pd
import os
import cv2
full_path_to_ts_dataset = 'C:\Users\Varang Rai\Desktop\Dataset\FullIJCNN2013'


# Reading txt file with annotations separated by semicolons
ann = pd.read_csv(full_path_to_ts_dataset + '/' + 'gt.txt',
                  names=['ImageID',
                         'XMin',
                         'YMin',
                         'XMax',
                         'YMax'],
                  sep=';')

ann['center x'] = ''
ann['center y'] = ''
ann['width'] = ''
ann['height'] = ''

# Calculating bounding box's center in x and y for all rows
# Saving results to appropriate columns
ann['center x'] = (ann['XMax'] + ann['XMin']) / 2
ann['center y'] = (ann['YMax'] + ann['YMin']) / 2
# Calculating bounding box's width and height for all rows
# Saving results to appropriate columns
ann['width'] = ann['XMax'] - ann['XMin']
ann['height'] = ann['YMax'] - ann['YMin']
r = ann.loc[:, ['ImageID',
                'center x',
                'center y',
                'width',
                'height']].copy()
"""
Normalizing YOLO numbers according to the real image width and height
Saving annotations in txt files
Converting images from ppm to jpg
"""
# Changing the current directory
# to one with images
os.chdir(full_path_to_ts_dataset)

# Using os.walk for going through all directories and files in them from the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.ppm'
        if f.endswith('.ppm'):
            # Reading image and getting its real width and height
            image_ppm = cv2.imread(f)
            # Slicing from tuple only first two elements
            h, w = image_ppm.shape[:2]
            # Slicing only name of the file without extension
            image_name = f[:-4]
            sub_r = r.loc[r['ImageID'] == f].copy()

            # Normalizing calculated bounding boxes' coordinates
            # according to the real image width and height
            sub_r['center x'] = sub_r['center x'] / w
            sub_r['center y'] = sub_r['center y'] / h
            sub_r['width'] = sub_r['width'] / w
            sub_r['height'] = sub_r['height'] / h
            resulted_frame = sub_r.loc[:, ['center x',
                                           'center y',
                                           'width',
                                           'height']].copy()

            # Checking if there is no any annotations for current image
            if resulted_frame.isnull().values.all():
                # Skipping this image
                continue
            path_to_save = full_path_to_ts_dataset + '/' + image_name + '.txt'
            resulted_frame.to_csv(path_to_save, header=False, index=False, sep=' ')
            path_to_save = full_path_to_ts_dataset + '/' + image_name + '.jpg'
            cv2.imwrite(path_to_save, image_ppm)
