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


def get_contours_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if(M['m00'] != 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return cx, cy


def process_contours(binary_image, rgb_image, contours):
    black_image = np.zeros(
        [binary_image.shape[0], binary_image.shape[1], 3], np.uint8)
    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if area > 1000:
            cv2.drawContours(rgb_image, [c], -1, (150, 250, 150), 1)
            cv2.drawContours(black_image, [c], -1, (150, 250, 150), 1)
            cx, cy = get_contours_center(c)
            #cv2.circle(rgb_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
            cv2.circle(black_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
        print ("Area :{}, Perimeter:{}".format(area, perimeter))
    print("number of contours:{}".format(len(contours)))
    cv2.imshow("Process RGB Image Contours", rgb_image)
    cv2.imshow("Process Black Image Contours", black_image)


def main():
    image_name = "images/105.jpg"
    rgb_image = read_image(image_name, False)
    gray_image = convert_rgb_to_gray(rgb_image, False)
    binary_image = convert_gray_to_binary(gray_image, True, False)
    contours = get_contours(binary_image)
    #draw_contours(rgb_image, contours, "RGB_Contours")
    #draw_contours(binary_image, contours, "Binary_Contours")
    process_contours(binary_image, rgb_image, contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
