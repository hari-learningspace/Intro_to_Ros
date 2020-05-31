#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def move():
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # initialize ros node
    rospy.init_node('move', anonymous=True)
    # set time loop rate
    rate = rospy.Rate(10)
    # Keep on Publishing the data

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.5
        twist.angular.z = -0.2
        speed_pub.publish(twist)
        rate.sleep()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
