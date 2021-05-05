# DeepTrafficSignDNC- Traffic Sign Detection and Classification

# 1. Contents

a- Overview

b- Detection

c- Classification


# 2. Overview

Some basic info what the project is

Sample results

# 3. Detection Pipeline:

### 3.1 Dataset used:

//Add citations, RP
*GTSDB - German Traffic Sign Detection Benchmark*
* 900 Scenic Images with annotations for bounding boxe
* 4 classes for traffic sign


### 3.2 Framework used:

list of frameworks with hyperlink/boxes

### 3.3 Training DarkNet YOLOv3

-- About the data prepration files, required for YOLO

### 3.4 Results

//GIF/images

## 4. Classification Pipeline:

### 4.1 Dataset used:

//Add citations, RP
- Russian Chinese German etc
* Total 80 indian classes


### 4.2 Framework used:

list of frameworks with hyperlink/boxes

### 4.3 Training DarkNet YOLOv3

-- About the data prepration files, required for YOLO

### 4.4 Results

//GIF/images

## 5. Detection and Classification

- The Idea is to process each frame using through a YOLO network, getting ROI of traffic sign, followed by feeding it to the classification model.
- OpenCV deep neural network library was used to import YOLO model, feeding to it the weights of YOLOv3 trained in darknet.

### Results

** Using Colab GPU's the model performed at an average rate of 60 fps giving a classification accuracy of ~80%.** 
