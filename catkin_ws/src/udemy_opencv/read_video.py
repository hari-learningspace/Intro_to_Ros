#!/usr/bin/env python

import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # show only the gray scale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv2.line(frame, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.imshow("Frame", frame)

    # Delays the Key capture for 10ms
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
