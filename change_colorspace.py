#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import cv2
import numpy as np

print('####显示颜色空间####')
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

print('####object tracking####')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()