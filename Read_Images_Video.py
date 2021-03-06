# Reading an image

import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")  # Path to the image
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)

# Reading a Video

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/test_ video.mp4")   # Path to the video
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
         break
         
# Reading Web Cam

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)  # Default code '0', i.e for web cam
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
