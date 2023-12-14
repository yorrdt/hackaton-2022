import sys
import cv2
import numpy as np
import time

def add_HSV_Filter (frame, camera):
    
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    return blur