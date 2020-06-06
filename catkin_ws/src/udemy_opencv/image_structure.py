#!/usr/bin/env python
import numpy as np
import cv2

# open image
img = cv2.imread("images/101.jpg")

print "image size -", img.size
print"image shape - ", img.shape
print"image height - ", img.shape[0]
print"image width - ", img.shape[1]
print"image channels - ", img.shape[2]
print "nump array"
print img
print img.dtype
print img[0]
print img[0][0]
print img[:][:][0]
