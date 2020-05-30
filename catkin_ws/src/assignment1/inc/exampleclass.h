#ifndef EXAMPLE_ROS_CLASS_H_
#define EXAMPLE_ROS_CLASS_H_

#include <math.h>
#include <stdlib.h>
#include <string>
#include <vector>

#include <ros/ros.h>

#include <geometry_msgs/Twist.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Float32.h>
#include <std_srvs/Trigger.h>
#include <turtlesim/Pose.h>

class ExampleRosSubClass {
public:
  ExampleRosSubClass(ros::NodeHandle *nodehandle);

private:
  ros::NodeHandle nh_;
  ros::Subscriber minimal_subscriber_;

  // Methods
  void initializeSubscribers();
  void subscriberCallback(const turtlesim::Pose &message_holder);
};

class ExampleRosPubClass {
public:
  ExampleRosPubClass(ros::NodeHandle *nodehandle);
  void publish_cmd_vel(float x, float z);

private:
  ros::NodeHandle nh_;
  ros::Publisher minimal_publisher_;

  // Methods
  void initializePublishers();
};

#endif