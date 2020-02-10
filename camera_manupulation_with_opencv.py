# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:59:38 2020

@author: KIIT
"""
import matplotlib.pyplot as plt
import numpy as mp
import cv2

%matplotlib inline
"""CAMERA = cv2.VideoCapture(0)

while (True):

    #read a new frame
    _, frame = CAMERA.read()

    #show the frame
    cv2.imshow("Capturing frames", frame)

    #quit camera if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

CAMERA.release()
cv2.destroyAllWindows()"""

CAMERA = cv2.VideoCapture(0)
HEIGHT = 500
RAW_FRAMES = []

while(True) :
    #read a frame
    _, frame = CAMERA.read()

    #flip the frame
    frame = cv2.flip (frame, 1)

    #rescaling camera output
    aspect = frame.shape[1]/ float(frame.shape[0])
    res = int(aspect * HEIGHT) #landscape orientation - wide Image
    frame = cv2.resize(frame, (res, HEIGHT))

    #add rectangle
    cv2.rectangle(frame, (300, 75), (650, 425), (0, 255, 0), 2)

    #show the frame
    cv2.imshow("Capturing frame", frame)
    
    key =cv2.waitKey(1)
    #quit camera if 'q' key is pressed
    
    if key & 0xff == ord("q"):
        break
    
    elif key & 0xFF ==ord("s"):
        RAW_FRAMES.append(frame)
        
        plt.imshow(frame)
        plt.show()

CAMERA.release()
cv2.destroyAllWindows()


IMAGES =[]
for frame in RAW_FRAMES:
    roi = frame[75+1:425-1,300+1:650-1]
    
    IMAGES.append(roi)
    
    plt.imshow(roi)
    plt.show()