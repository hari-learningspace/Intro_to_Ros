#!/usr/bin/env python

from udemy_rosservice.srv import addtwoints
from udemy_rosservice.srv import addtwointsRequest
from udemy_rosservice.srv import addtwointsResponse

import rospy


def service_callback_function(request_messsage):
    print "Returning [%s + %s = %s]" % (request_messsage.x, request_messsage.y, (request_messsage.x + request_messsage.y))
    return addtwointsResponse(request_messsage.x + request_messsage.y)


def add_two_ints_server_node():
    rospy.init_node('add_two_ints_server_node')
    s = rospy.Service('add_two_ints', addtwoints, service_callback_function)
    print "Server Ready to add two ints"
    rospy.spin()


if __name__ == '__main__':
    add_two_ints_server_node()
