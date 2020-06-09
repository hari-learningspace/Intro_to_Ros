#!/usr/bin/env python
import numpy as np
import cv2


def read_image(image_name, show):
    image = cv2.imread(image_name, cv2.IMREAD_COLOR)
    if show:
        cv2.imshow("RGB Image", image)
    return image


def convert_rgb_to_gray(image, show):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if show:
        cv2.imshow("Gray Image", gray_image)
    return gray_image


def convert_gray_to_binary(image, adaptive, show):
    if adaptive:
        binary_image = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 2)
    else:
        binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    if show:
        cv2.imshow("Binary Image", binary_image)
    return binary_image


def get_contours(binary_image):
    _, contours, _ = cv2.findContours(
        binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def draw_contours(image, contours, image_name):
    index = -1
    thickness = 2
    color = (255, 0, 255)
    cv2.drawContours(image, contours, index, color, thickness)
    cv2.imshow(image_name, image)


def main():
    image_name = "images/105.jpg"
    rgb_image = read_image(image_name, True)
    gray_image = convert_rgb_to_gray(rgb_image, True)
    binary_image = convert_gray_to_binary(gray_image, True, True)
    contours = get_contours(binary_image)
    draw_contours(rgb_image, contours, "RGB_Contours")
    draw_contours(binary_image, contours, "Binary_Contours")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
