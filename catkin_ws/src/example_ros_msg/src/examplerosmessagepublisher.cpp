#include <ros/ros.h>
#include <example_ros_msg/ExampleMessage.h>
#include <math.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "example_ros_publisher");
    ros::NodeHandle nh;
    ros::Publisher my_pub=nh.advertise<example_ros_msg::ExampleMessage>("example_topic",1);

    example_ros_msg::ExampleMessage my_message;

    ros::Rate naptime(1);

    my_message.header.stamp = ros::Time::now();
    my_message.header.frame_id= "base_frame";
    my_message.header.seq=0;

    my_message.demo_double=100.0;
    my_message.demo_int = 1;

    double sqrt_arg;

    while(1)
    {
        my_message.header.seq++;
        my_message.header.stamp = ros::Time::now();
        my_message.demo_int *= 2;
        
        sqrt_arg = my_message.demo_double;
        my_message.demo_double = sqrt(sqrt_arg);

        my_pub.publish(my_message);

        naptime.sleep();

    }
}
