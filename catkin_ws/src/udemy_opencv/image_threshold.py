#!/usr/bin/env python
import numpy as np
import cv2


def read_image(image_name, as_gray):
    if as_gray:
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
    return image


def basic_thresholding(gray_image, thresol_value):
    ret, thresh_basic = cv2.threshold(
        gray_image, thresol_value, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Basic Binary Image", thresh_basic)


def adaptive_thresholding(gray_image, thresol_value):
    adaptive_thresh_image = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, thresol_value, 2)
    cv2.imshow("Adaptive Threshold Image", adaptive_thresh_image)


def main():
    image_name = "images/101.jpg"
    as_gray = True
    threshol_value = 205
    gray_image = read_image(image_name, as_gray)
    basic_thresholding(gray_image, threshol_value)
    adaptive_thresholding(gray_image, threshol_value)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
