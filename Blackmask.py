import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_black = np.array([0,0,0])
    upper_black = np.array([340,55,100])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_black, upper_black)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.waitKey(0)
cv.destroyAllWindows()