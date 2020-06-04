# Drawing Shapes and text on a blank image

import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)  # Creating the blank image
#print(img)
#img[:]= 255,0,0
 
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  # Drawing Lines
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)   # Drawing Rectangles
cv2.circle(img,(400,50),30,(255,255,0),5)   # Drawing Circles
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)   # Writing on the image
 
cv2.imshow("Image",img)
cv2.waitKey(0)
