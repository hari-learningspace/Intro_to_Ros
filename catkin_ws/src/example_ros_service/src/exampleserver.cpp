#include <ros/ros.h>
#include <example_ros_service/exampleservice.h>
#include <iostream>
#include <string>


bool callback(example_ros_service::exampleserviceRequest &request, 
                example_ros_service::exampleserviceResponse &response)
{
    ROS_INFO("callback activated");
    std::string in_name(request.name);  //copying the request to local string

    response.on_the_list = false;

    if(in_name.compare("Bob") == 0)
    {
        ROS_INFO("asked about Bob");
        response.age = 23;
        response.good_guy = true;
        response.on_the_list = true;
        response.nickname = "Bob The Terrible";
    }

    if(in_name.compare("Ted") == 0)
    {
        ROS_INFO("asked about Ted");
        response.age = 21;
        response.good_guy = true;
        response.on_the_list = true;
        response.nickname = "Ted the Benevolent";
    }
    return true;

}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "example_ros_service");
    ros::NodeHandle nh;

    ros::ServiceServer service = nh.advertiseService("lookup_by_name", callback);
    ROS_INFO("Ready to Look Up Name");
    ros::spin();

    return 0;

}
