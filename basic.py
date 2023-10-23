import cv2 as cv

img =cv.imread('photo/rabbit.jpg')
cv.imshow("rabit",img)

#convering to grayscale
# gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

#blur
# blur = cv.GaussianBlur(img,(21,21),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#edge cascade
# canny =cv.Canny(img,125,175)
# cv.imshow('canny edges',canny)

#Dilating the image
# dilated = cv.dilate(canny,(3,3),iterations=4)
# cv.imshow("dilated",dilated)
#
# eroding
# eroded = cv.erode(dilated,(3,3),iterations=4)
# cv.imshow("eroded",eroded)

#resize
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow("resized",resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)