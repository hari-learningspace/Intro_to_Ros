#!/usr/bin/env python
import numpy as np
import cv2


def main():
    image_name = "images/102.jpg"
    original_image = cv2.imread(image_name)
    cv2.imshow("original image", original_image)

    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    cv2.imshow("HSV Image", hsv_image)

    # Lower and Uppper Bound
    yellowlower = (30, 80, 80)
    yellowupper = (60, 255, 255)

    mask = cv2.inRange(hsv_image, yellowlower, yellowupper)
    cv2.imshow("mask_image", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
