import cv2 as cv

img = cv.imread('photos/cachorro.jpg')

cv.imshow('dog', img)

cv.waitKey(0)