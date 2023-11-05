import cv2 as cv

img = cv.imread('photo/cat.jpg')
cv.imshow("cats",img)

#average
average = cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

#gaussian
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Blur",gauss)

#Median
median =cv.medianBlur(img, 3)
cv.imshow("median Blur",median)

#biloteral
biloteral = cv.bilateralFilter(img, 5, 15,15)
cv.imshow("biloteral",biloteral)


cv.waitKey(-1)