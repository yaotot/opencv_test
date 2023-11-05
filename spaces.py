import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photo/rabbit.jpg')
cv.imshow("rabbit",img)

plt.imshow(img)
plt.show()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#BGR to HSV
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#BGR to LAB
lab= cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)


#BGR 2 RGB
rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)


cv.waitKey(-1)

