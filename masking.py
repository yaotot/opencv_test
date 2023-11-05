import cv2 as cv
import numpy as np


img = cv.imread('photo/cat.jpg')
cv.imshow('cats',img)

blank =np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank image',blank)

#circle = cv.circle(blank.copy,(img.shape[1]//2,img.shape[0]//2), 100, 255 ,-1)

rectangle =cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)

masked = cv.bitwise_and(img,img, mask=rectangle)
cv.imshow("masked img", masked)

cv.waitKey(-1)