#!/usr/bin/env python
import rospy
from udemy_rosmsg.msg import iotsensor
import random


pub = rospy.Publisher('iot_sensor_topic', iotsensor, queue_size=10)
# initialize ros node
rospy.init_node('iot_sensor_pub_node', anonymous=True)
# set time loop rate
rate = rospy.Rate(10)
# Keep on Publishing the data
i = 0
while not rospy.is_shutdown():
    iot_sensor_data = iotsensor()
    iot_sensor_data.id = 1
    iot_sensor_data.name = "iot_parking_01"
    iot_sensor_data.temperature = 24.33 + (random.random()*2)
    iot_sensor_data.humidity = 33.41 + (random.random()*2)
    rospy.loginfo("I Publish")
    rospy.loginfo(iot_sensor_data)
    pub.publish(iot_sensor_data)
    i += 1
    rate.sleep()
