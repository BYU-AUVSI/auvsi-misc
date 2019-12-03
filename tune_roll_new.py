#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Internal_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('TUNE_ROLL', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'internal_commands')
    center_roll = rospy.get_param('~roll', 0.0)
    amplitude = rospy.get_param('~amplitude', 10)
    period = rospy.get_param('~period', 20)

    command_pub = rospy.Publisher(command_topic, Internal_Commands, queue_size=1)

    command = Internal_Commands()
    command.tuning_zone = 4 # TUNE_ROLL

    rate = rospy.Rate(2./period)
    fast = True
    while not rospy.is_shutdown():
        if fast:
            command.phi_c = center_roll + amplitude/2
        else:
            command.phi_c = center_roll - amplitude/2
        command_pub.publish(command)
        fast = not fast
        rate.sleep()

if __name__=='__main__':
    main()