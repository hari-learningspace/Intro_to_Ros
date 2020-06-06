#!/usr/bin/env python

# OpenCV Libaries
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Ros Libaries
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

# System Libraries
import sys


# Bridge for Converting sensor_msgs to opencv format
bridge = CvBridge()


def image_callback(ros_image):
    print "got an image"
    global bridge
    # convert the image
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)


def main(args):
    rospy.init('image_converter', anonymous-True)
    image_sub = rospy.Subscriber('usb_cam/image_raw', Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")


if __name__ == '__main__':
    main(sys.argv)
