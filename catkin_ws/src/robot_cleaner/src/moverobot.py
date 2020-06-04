#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

# Save the Orientation Received from Subscriber
x = 0
y = 0
yaw = 0
counter = 0


def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta


def move(speed, distance, isForward):
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # set time loop rate
    rate = rospy.Rate(100)

    if(isForward):
        vel_msg.linear.x = abs(speed)
        logmsg = "Turlte Sim Moves Forward"
    else:
        vel_msg.linear.x = -abs(speed)
        logmsg = "Turlte Sim Moves Reverse"

    t0 = rospy.get_rostime()
    distance_moved = 0.0
    while True:
        rospy.loginfo(logmsg)
        vel_pub.publish(vel_msg)
        rate.sleep()
        t1 = rospy.get_rostime()
        distance_moved = speed * (t1.secs - t0.secs)
        print(distance_moved)
        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break
    # Stop the Robot when the distance reached
    vel_msg.linear.x = 0
    vel_pub.publish(vel_msg)


def rotate(angularspeed, angle, isClockWise):
    # set time loop rate
    rate = rospy.Rate(100)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    if(isClockWise):
        vel_msg.angular.z = -abs(math.radians(angularspeed))
    else:
        vel_msg.angular.z = abs(math.radians(angularspeed))

    t0 = rospy.Time.now().to_sec()
    current_angle = 0.0
    while True:
        vel_pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angularspeed * (t1 - t0)
        rate.sleep()
        print(current_angle, angle)
        if (current_angle > angle):
            rospy.loginfo("angle reached")
            break

    # Stop the Robot when the distance reached
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)


def degree_in_radians(angle_in_degree):
    return (angle_in_degree*3.142)/180.0


def set_desired_orientation(desired_angle_degree):
    req_angle = desired_angle_degree
    while req_angle >= 360:
        req_angle -= 360

    relative_angle_degree = req_angle - math.degrees(turtlesim_pose.theta)
    if (relative_angle_degree < 0):
        clockwise = True
    else:
        clockwise = False
    rotate(abs(relative_angle_degree), abs(relative_angle_degree), clockwise)


def go_to_goal(goal_x, goal_y):
    global x, y, yaw
    vel_message = Twist()

    while(True):
        k_linear = 0.5
        distance = abs(math.sqrt(((goal_x-x) ** 2) + ((goal_y-y)**2)))
        linear_speed = distance * k_linear

        k_angular = 4.0
        desired_goal_angle = math.atan2(goal_y-y, goal_x-x)
        angular_speed = (desired_goal_angle-yaw)*k_angular

        vel_message.linear.x = linear_speed
        vel_message.angular.z = angular_speed
        vel_pub.publish(vel_message)

        print(distance, angular_speed)
        print(x, y)
        if(distance < 0.01):
            print("reached")
            break
    vel_message.linear.x = 0
    vel_message.angular.z = 0
    vel_pub.publish(vel_message)


if __name__ == '__main__':
    # initialize ros node
    rospy.init_node('robot_cleaner', anonymous=True)

    # cmd_vel topic
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # cmd_vel topic
    orient_sub = rospy.Subscriber('/turtle1/pose', Pose, poseCallback)
    time.sleep(2)
    # move(1, 4, 0)
    #rotate(90, 90, 0)
    # set_desired_orientation(0)
    x_goal = rospy.get_param("x_goal")
    y_goal = rospy.get_param("y_goal")
    go_to_goal(10.0, 10.0)
