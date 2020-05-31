#!/usr/bin/env python

from udemy_rosservice.srv import addtwoints
from udemy_rosservice.srv import addtwointsRequest
from udemy_rosservice.srv import addtwointsResponse

import rospy
import sys


def add_two_ints_client_node(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', addtwoints)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed :%s" % e


def usage():
    return "%s [x y]" % sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s + %s" % (x, y)
    print "%s + %s = %s" % (x, y, add_two_ints_client_node(x, y))
