#!/usr/bin/env python

import numpy as np
import cv2

image_name = "101"

print 'read an image from file'
color_image = cv2.imread("images/101.jpg", cv2.IMREAD_COLOR)

print 'display image in native color'
cv2.imshow("original image", color_image)
cv2.moveWindow("original image", 0, 0)
print(color_image.shape)

height, width, channels = color_image.shape
print 'slip image into three channels'

blue, green, red = cv2.split(color_image)

cv2.imshow("Blue Channel", blue)
cv2.moveWindow("Blue Channel", 0, height)

cv2.imshow("Red Channel", red)
cv2.moveWindow("Red Channel", 0, height)

cv2.imshow("Green Channel", green)
cv2.moveWindow("Green Channel", 0, height)

# HSV image
hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_image = np.concatenate((h, s, v), axis=1)
cv2.imshow("Hue Saturation, Value image", hsv_image)

# gray scale image
print"----------------converts an image to grayscale---------------"
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image ", gray_image)
print gray_image.shape
print gray_image

cv2.waitKey(0)
cv2.destroyAllWindows()
