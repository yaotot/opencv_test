import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank', blank)

#1.paint the image a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green',blank)

#2. Draw a Rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow("rectangle", blank)

#3. draw circle
# cv.circle(blank, (255,255),100,(0,0,255),thickness=-1)
# cv.imshow('circle', blank)

#4.draw line
# cv.line(blank,(0,0),(255,260),(255,3,5),thickness=3)
# cv.imshow("line",blank)

#write text
cv.putText(blank,'hello,cool',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,3),2)
cv.imshow("text",blank)

cv.waitKey(0)