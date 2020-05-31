#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose


def callback(data):
    rospy.loginfo(data)


def getposition():
    # init ros node
    rospy.init_node('getposition', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)

    rospy.spin()


if __name__ == "__main__":
    getposition()
