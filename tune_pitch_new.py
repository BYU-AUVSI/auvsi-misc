#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Internal_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('TUNE_PITCH', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'internal_commands')
    center_pitch = rospy.get_param('~pitch', 0.0)
    amplitude = rospy.get_param('~amplitude', 5.0*pi/180.0)
    period = rospy.get_param('~period', 20)

    command_pub = rospy.Publisher(command_topic, Internal_Commands, queue_size=1)

    command = Internal_Commands()
    command.tuning_zone = 1 # TUNE_PITCH

    rate = rospy.Rate(2./period)
    fast = True
    while not rospy.is_shutdown():
        if fast:
            command.theta_c = center_pitch + amplitude/2
        else:
            command.theta_c = center_pitch - amplitude/2
        command_pub.publish(command)
        fast = not fast
        rate.sleep()

if __name__=='__main__':
    main()