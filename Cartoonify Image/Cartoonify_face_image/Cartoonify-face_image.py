#Importing required libraries
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

#Reading image 
img = cv2.imread("face.jpg")
from skimage import io 
io.imshow(img)

#Converting to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
io.imshow(img)

#Detecting edges of the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
io.imshow(edges)

#Cartoonifying the image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

io.imshow(cartoon)

