

"""
Converting Traffic Signs dataset in YOLO format
"""

# Creating files ts_data.data and classes.names
# for training in Darknet framework
#
# Algorithm:
# Setting up full path --> Reading file classes.txt -->
# --> Creating file classes.names -->
# --> Creating file ts_data.data
#
# Result:
# Files classes.names and ts_data.data needed to train
# in Darknet framework


full_path_to_images = 'C:\Users\Varang Rai\Desktop\Dataset\ts'
# Defining counter for classes
c = 0
with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:
    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names
        # Increasing counter
        c += 1

"""
Created classes.names
"""

"""
Creating file ts_data.data
"""

with open(full_path_to_images + '/' + 'ts_data.data', 'w') as data:
    data.write('classes = ' + str(c) + '\n')
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')
    data.write('backup = backup')
