#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Controller_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('TUNE_ALTITUDE', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'internal_commands')
    command_airspeed = rospy.get_param('~airspeed', 15.0)
    center_altitude = rospy.get_param('~center_altitude',180.0)
    amplitude = rospy.get_param('~amplitude', 4.0)
    period = rospy.get_param('~period', 20)

    command_pub = rospy.Publisher(command_topic, Internal_Commands, queue_size=1)
    neg_alt_pub = rospy.Publisher('negative_altitude_command', std_msgs.msg.Float32, queue_size = 1)

    command = Internal_Commands()
    command.Va_c = command_airspeed
    command.tuning_zone = 3 # TUNE_ALTITUDEw

    neg_alt_msg = std_msgs.msg.Float32()

    rate = rospy.Rate(2./period)
    up = True
    while not rospy.is_shutdown():
        if up:
            command.h_c = center_altitude + amplitude/2
        else:
            command.h_c = center_altitude - amplitude/2
        neg_alt_msg.data = -command.h_c
        command_pub.publish(command)
        neg_alt_pub.publish(neg_alt_msg)
        up = not up
        print("pub", command.h_c)
        rate.sleep()

if __name__=='__main__':
    main()
