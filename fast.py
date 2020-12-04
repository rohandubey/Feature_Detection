import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('sample2.png',0)
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
cv2.imshow('dst',img2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
cv2.imshow('dst',img3)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
