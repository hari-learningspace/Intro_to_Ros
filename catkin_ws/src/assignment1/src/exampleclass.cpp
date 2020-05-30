#include <exampleclass.h>

ExampleRosSubClass::ExampleRosSubClass(ros::NodeHandle *nodeHandle)
    : nh_(*nodeHandle) {
  ROS_INFO("ROS Class Node - With Subscriber");
  initializeSubscribers();
}

ExampleRosPubClass::ExampleRosPubClass(ros::NodeHandle *nodeHandle)
    : nh_(*nodeHandle) {
  ROS_INFO("ROS Class Node - With Publisher");
  initializePublishers();
}

void ExampleRosSubClass::initializeSubscribers() {
  ROS_INFO("Initialize Subscribers");
  minimal_subscriber_ = nh_.subscribe(
      "/turtle1/pose", 1, &ExampleRosSubClass::subscriberCallback, this);
}

void ExampleRosPubClass::initializePublishers() {
  ROS_INFO("Initialize Publishers");
  minimal_publisher_ =
      nh_.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1, true);
}

void ExampleRosSubClass::subscriberCallback(
    const turtlesim::Pose &message_holder) {
  ROS_INFO("Turtlesim is Moving");
  ROS_INFO("Linear x : %f", message_holder.linear_velocity);
  ROS_INFO("Angular x : %f", message_holder.angular_velocity);
}

void ExampleRosPubClass::publish_cmd_vel(float x, float z) {
  ROS_INFO("publish x and z position");
  geometry_msgs::Twist position;
  position.linear.x = x;
  position.linear.z = z;

  minimal_publisher_.publish(position);
}