#include <exampleclass.h>

int main(int argc, char **argv) {
  ros::init(argc, argv, "Publisher_Node");

  ros::NodeHandle pnh;

  ROS_INFO("Main:Instantiating an object of type ExampleRosPubClass");

  ExampleRosPubClass exampleRosPubClass(&pnh);

  ros::Rate naptime(1);

  while (1) {

    for (float i = 0; i <= 1.0; i += 0.5) {
      exampleRosPubClass.publish_cmd_vel(i, (i - 0.5));
      naptime.sleep();
    }
  }

  return 0;
}