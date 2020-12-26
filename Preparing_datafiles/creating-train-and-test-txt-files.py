# Converting Traffic Signs dataset in YOLO format

# Creating files train.txt and test.txt
# for training in Darknet framework
#
# Algorithm:
# Setting up full path --> List of paths -->
# --> Extracting 15% of paths to save into test.txt file -->
# --> Writing paths into train and test txt files
#
# Result:
# Files train.txt and test.txt with full paths to images
# Importing needed library
import os

full_path_to_images = 'C:\Users\Varang Rai\Desktop\Dataset\ts'
os.chdir(full_path_to_images)
# Defining list to write paths in
p = []
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpg'
        if f.endswith('.jpg'):
            path_to_save_into_txt_files = full_path_to_images + '/' + f
            p.append(path_to_save_into_txt_files + '\n')
p_test = p[:int(len(p) * 0.15)]
# Deleting from initial list first 15% of elements
p = p[int(len(p) * 0.15):]

"""
Creating train.txt and test.txt files
"""
# Creating file train.txt and writing 85% of lines in it
with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        train_txt.write(e)
# Creating file test.txt and writing 15% of lines in it
with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)
