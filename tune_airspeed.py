#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Controller_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('altitude_tuner', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'controller_commands')
    center_airspeed = rospy.get_param('~airspeed', 30.0)
    command_altitude = rospy.get_param('~center_altitude', 50.0)
    amplitude = rospy.get_param('~amplitude', 2)
    period = rospy.get_param('~period', 20)
    command_course = rospy.get_param('~course', pi/2)

    command_pub = rospy.Publisher(command_topic, Controller_Commands, queue_size=1)

    command = Controller_Commands()
    command.h_c = command_altitude
    command.chi_c = command_course
    command.aux_valid = False

    neg_alt_msg = std_msgs.msg.Float32()
    
    rate = rospy.Rate(2./period)
    fast = True
    while not rospy.is_shutdown():
        if fast:
            command.Va_c = center_airspeed + amplitude/2
        else:
            command.Va_c = center_airspeed - amplitude/2
        command_pub.publish(command)
        fast = not fast
        rate.sleep()

if __name__=='__main__':
    main()
