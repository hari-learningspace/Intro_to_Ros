#include <exampleclass.h>

int main(int argc, char **argv) {
  ros::init(argc, argv, "Subscriber_Node");

  ros::NodeHandle snh;

  ROS_INFO("Main:Instantiating an object of type ExampleRosClass");

  ExampleRosSubClass exampleRosSubClass(&snh);

  ROS_INFO("main: going into spin: let the callback do all the work");

  ros::spin();

  return 0;
}