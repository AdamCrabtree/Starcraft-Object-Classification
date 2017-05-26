import os as os
import cv2 as cv2
img = cv2.imread('hive.png',0)
resized_image = cv2.resize(img, (50,50))
cv2.imwrite("pos/HiveResized.jpg", resized_image)

