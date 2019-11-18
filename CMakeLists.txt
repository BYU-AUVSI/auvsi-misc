cmake_minimum_required(VERSION 2.8.3)
project(auvsi_misc)

find_package(catkin REQUIRED COMPONENTS
  rospy
  rosplane
)


catkin_package(
  CATKIN_DEPENDS rospy rosplane
)

include_directories(include)
include_directories(
   ${catkin_INCLUDE_DIRS}
)
