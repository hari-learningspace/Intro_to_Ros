#!/usr/bin/env python

import numpy as np
import cv2

# Creat a Image with Pixel 512x512 RGB
image = np.zeros((512, 512, 3), np.uint8)


# Pt Definition
# x0y0, x1y0, x2 y0
# x0y1 , x1y1, x2y1
# Draw a Line in the Middle of the image
# Start Co-ordinate end Co-ordinate While Color and Line Width
cv2.line(image, (0, 0), (512, 0), (255, 255, 255), 5)

cv2.line(image, (0, 50), (512, 50), (255, 255, 255), 5)

# Draw Rectange
cv2.rectangle(image, (256, 0), (400, 256), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "ROS OpenCV", (10, 500),
            font, 2, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("Draw Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
