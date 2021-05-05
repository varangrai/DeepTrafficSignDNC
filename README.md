# TrafficSignNet
A first of a kind Indian traffic sign detector.

## Dataset used:
1. *Russian Traffic Sign Dataset (RTSD)* - 
* 179138 labelled frames,
* 156 sign classes,
* 15630 physical signs,
* 104358 images of signs.
2. *GTSDB - German Traffic Sign Detection Benchmark*
* 900 Scenic Images with annotations for bounding boxe
* 4 classes for traffic sign
3. *Chinese Traffic Sign Database* 
* TSRD has 6164 traffic sign images containing 58 sign categories. 
* The training database includes 4170 images while the testing one contains 1994 images. All images are annotated the four corrdinates of the sign and the category.

## Detection Pipeline:
* Detection is based on YOLOv3 model trained in darknet framework, 1ith target labels as bounding box annotations converted to YOLO format
* Trained for ~1000 iterations on GTSDB
## Classification Pipeline:
There are 2 main approaches based on 
1. One Shot Learning: Using a Siamese network to get a 64 dimension embedding. Training was done on ~20000 traffic signs of many conutries,  
minimizing triplet loss function. After getting optimal weights, embedding of 1 image of each class was saved, now test image's L2 distance is calculated, 
and the nearest embedding's label is the prediction.
2. Using CNN: Training a CNN on the similar looking traffic signs of various other countries, and using ImgAug library to improve further accuracy.
## Detection + Classification on Video:
- The Idea is to process each frame using through a YOLO network, getting ROI of traffic sign, followed by feeding it to the classification model.
- OpenCV deep neural network library was used to import YOLO model, feeding to it the weights of YOLOv3 trained in darknet.

** Using Colab GPU's the model performed at an average rate of 60 fps giving a classification accuracy of ~80%.** 
