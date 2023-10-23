import cv2 as cv

img = cv.imread('photo/rabbit.jpg')
cv.imshow("rabbit",img)
cv.waitKey(0)