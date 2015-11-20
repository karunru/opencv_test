import numpy as np
import cv2

img = cv2.imread('test.png',0)
img_gray = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
cv2.imwrite("detected.jpg", img_gray)
#cv2.imwrite("detected.jpg", img)
