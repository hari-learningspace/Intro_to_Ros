#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def utalker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # initialize ros node
    rospy.init_node('talker', anonymous=True)
    # set time loop rate
    rate = rospy.Rate(10)
    # Keep on Publishing the data
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        utalker()
    except rospy.ROSInterruptException:
        pass
