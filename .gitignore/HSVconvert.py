# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:14:20 2020

@author: Harish
"""

import cv2
import numpy as np

"cap = cv2.VideoCapture(0)"

#while(1):

    # Take each frame
frame = cv2.imread(r'C:\Users\Harish\Desktop\Plant project\thespartans\.gitignore\test6.jpg')

    # Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
lower_green = np.array([30,100,100])
upper_green = np.array([70,225,225])

    # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
k = cv2.waitKey(5) & 0xFF
#if k == 27:
 #   break

"cv2.destroyAllWindows()"