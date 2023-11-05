import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle =cv.rectangle(blank.copy(), (30,30), (370,370), 100, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)



cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

#bitwise and
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise And',bitwise_and)

#bitwise or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise',bitwise_or)

#bitwise_xor
bitwise_xor =cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise xor", bitwise_xor)

#bitwise-not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise not',bitwise_not)


cv.waitKey(-1)