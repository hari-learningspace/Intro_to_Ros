#include <ros/ros.h>
#include <example_ros_service/exampleservice.h>
#include <iostream>
#include <string>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "example_ros_client");
    ros::NodeHandle nh;

    ros::ServiceClient client = nh.serviceClient<example_ros_service::exampleservice>("lookup_by_name");
    example_ros_service::exampleservice srv;

    bool found_on_list = false;
    std::string in_name;

    while(ros::ok())
    {
        std::cout << std::endl;
        std::cout << "Enter a name(x to quit):";
        std::cin >> in_name;
        if(in_name.compare("x") == 0){
            return 0;
        }
        srv.request.name = in_name;
        if(client.call(srv)){
            if(srv.response.on_the_list){
                std::cout << srv.request.name << " is Know as " << srv.response.nickname << std::endl;
                std::cout << "His age:"  << srv.response.age << std:: endl;
                if(srv.response.good_guy){
                    std::cout << "He is a good guy" << "\n";
                } else {
                    std::cout << "He is Bad, avoid him" << "\n";
                }
            } else {
                std::cout << srv.request.name << "is not in the list" << std::endl;
            } 
        } else {
            ROS_ERROR("Failed to call service look_by_name");
            return 1;
        }
    
    }
    return 0;
}

