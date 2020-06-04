# Resizing and cropping images

import cv2
import numpy as np
 
img = cv2.imread("Resources/lambo.png")  # The path to your image
print(img.shape)
 
imgResize = cv2.resize(img,(1000,500))  # Resizing the image
print(imgResize.shape)
 
imgCropped = img[0:200,200:500]  # Cropping the image
 
cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
 
cv2.waitKey(0)
