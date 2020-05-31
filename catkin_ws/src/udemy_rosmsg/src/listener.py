#!/usr/bin/env python
import rospy
from udemy_rosmsg.msg import iotsensor


def iot_sensor_callback(iotsensor_message):
    rospy.loginfo("new IoT Data Received :(%d, %s,%.2f, %.2f)",
                  iotsensor_message.id, iotsensor_message.name, iotsensor_message.temperature, iotsensor_message.humidity)


# init ros node
rospy.init_node('iotsensor_subscriber_node', anonymous=True)
rospy.Subscriber('iot_sensor_topic', iotsensor, iot_sensor_callback)

rospy.spin()
