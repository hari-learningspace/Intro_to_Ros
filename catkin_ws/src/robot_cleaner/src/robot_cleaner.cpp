#include "ros/ros.h"
#include <geometry_msgs/Twist.h>

double move(double speed, double distance, bool isForward);

int main(int argc, char **argv) {
  ros::init(argc, argv, "robot_cleaner");
  ros::NodeHandle nh;
}

double move(double speed, double distance, bool isForward) {
  geometry_msgs::Twist vel_msg;

  if (isForward) {

  }

  else {
    /* code */
  }
}