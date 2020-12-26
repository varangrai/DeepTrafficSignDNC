import os, pickle, shutil, csv, cv2, tensorflow as tf, numpy as np, matplotlib.pyplot as plt, seaborn as sns, skimage.morphology as morp
from skimage.io import imread
from skimage.filters import rank
from sklearn.utils import shuffle, compute_class_weight
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.models import Input, Model, load_model, Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.utils import to_categorical
from keras import optimizers
from keras.initializers import random_normal
from keras.callbacks import Callback, ReduceLROnPlateau, ModelCheckpoint
from sklearn.metrics import confusion_matrix
def show_images(data,y_data, label="", cmap=None, n_images = 10):
  plt.figure(figsize = (n_images*2,n_images*2))
  for i in range(n_images):
    plt.subplot(1,n_images,i+1)
    ind = np.random.randint(0,len(data))
    if len(data[ind].shape) == 2:
      cmap = 'gray'
    
    plt.imshow(data[ind],cmap = cmap)
   
    plt.ylabel(label, fontsize = 8)
    plt.xticks([])
    plt.yticks([])
  plt.tight_layout()
  plt.show()
def show_hist(data, label):
  plt.hist(data, bins = n_classes)
  plt.xlabel(label)
  plt.ylabel('class count')
  plt.grid('off')
  plt.show()
def convert_to_gray(image):
  return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
def norm_image(data):
  normalized_images = np.array(data,dtype = np.float32)/255
  return np.expand_dims(normalized_images, axis=-1)
def preprocess(x_data, n_classes = 70):
  gray_images = list(map(convert_to_gray,x_data))
  norm_images = norm_image(gray_images)
  return norm_images 
def VGG_variation(input_shape,nf=60):
  inputs = x = Input(input_shape)
  x = Conv2D(32, kernel_size = 3, padding = 'same',
                 activation = 'relu', 
                 kernel_initializer = random_normal(mean = 0,stddev = 0.1,))(x)
  x = MaxPooling2D(pool_size = 2, strides = 2, padding = 'valid')(x)
  x = Conv2D(64, kernel_size = 3, padding = 'same',
                  activation = 'relu', 
                  kernel_initializer = random_normal(mean = 0,stddev = 0.1,))(x)
  x = Conv2D(64, kernel_size = 3, padding = 'same',
                  activation = 'relu', 
                  kernel_initializer = random_normal(mean = 0,stddev = 0.1,))(x)
  x = Flatten()(x)
  #x = Dropout(0.5)(x)
  x = Dense(units = 128, activation = 'relu')(x)
  x= Dropout(0.3)(x)
  output = Dense(units = 70, activation = 'softmax')(x)
  VGG_var_model = Model(inputs = inputs, outputs = output)
  opti = optimizers.Adam(0.0001)
  VGG_var_model.compile(optimizer = opti, loss = 'categorical_crossentropy',
                       metrics = ['accuracy','categorical_crossentropy',tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
  return VGG_var_model
def scheduler(epoch, lr):
  if epoch < 50:
   return lr
  else:
   return 0.0001
  return model  
# def adapt_hist_equalization(image,clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(2,2))):
#   return clahe.apply(image)
# # Perform histogram equalization
# equalizied_gray_images = list(map(hist_equalization,gray_images))
# show_images(equalizied_gray_images,Y_train)