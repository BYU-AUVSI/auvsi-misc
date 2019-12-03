#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Internal_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('TUNE_COURSE', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'internal_commands')
    command_airspeed = rospy.get_param('~airspeed', 10.0)
    command_altitude = rospy.get_param('~altitude', 40.0)
    amplitude = rospy.get_param('~amplitude', 5.*pi/180)
    period = rospy.get_param('~period', 20)
    center_course = rospy.get_param('~center_course', 90*pi/180)

    command_pub = rospy.Publisher(command_topic, Internal_Commands, queue_size=1)

    command = Internal_Commands()
    command.Va_c = command_airspeed
    command.h_c = command_altitude
    command.tuning_zone = 5 # TUNE_COURSE

    neg_alt_msg = std_msgs.msg.Float32()

    rate = rospy.Rate(2./period)
    left = True
    while not rospy.is_shutdown():
        if left:
            command.chi_c = center_course + amplitude/2
        else:
            command.chi_c = center_course - amplitude/2
        command_pub.publish(command)
        left = not left
        rate.sleep()

if __name__=='__main__':
    main()
