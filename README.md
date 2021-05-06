# DeepTrafficSignDNC- Traffic Sign Detection and Classification

# Contents

a- Overview

b- Detection

c- Classification


# 1. Overview

This project aims to detect and clasify traffic signs in real time using YOLOv3 with darkNet framework for detection and a CNN for recognition purposes.

Sample results

# 2. Detection Pipeline:

### 2.1 Dataset used:

//Add citations, RP
*GTSDB - German Traffic Sign Detection Benchmark*
* 900 Scenic Images with annotations for bounding boxe
* 4 classes for traffic sign


### 2.2 Framework used:

list of frameworks with hyperlink/boxes

### 2.3 Training DarkNet YOLOv3

-- About the data prepration files, required for YOLO

### 2.4 Results

//GIF/images

## 3. Classification Pipeline:

### 3.1 Dataset used:

//Add citations, RP
- Russian Chinese German etc
* Total 80 indian classes


### 3.2 Framework used:

list of frameworks with hyperlink/boxes

### 3.3 Training DarkNet YOLOv3

-- About the data prepration files, required for YOLO

### 3.4 Results

//GIF/images

## 4. Detection and Classification

- The Idea is to process each frame using through a YOLO network, getting the ROI of traffic sign, followed by feeding it to the classification model.
- OpenCV deep neural network library was used to import YOLO model, feeding to it the weights of YOLOv3 trained in darknet.

### Results
** Speed of detection should be around 50 ms if everything works right with opencv gpu enabled
** Using Colab GPU's the model performed at an average rate of 60 fps giving a classification accuracy of ~80%.** 
