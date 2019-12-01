#!/usr/bin/env python
import rospy
from rosplane_msgs.msg import Internal_Commands
import std_msgs
from math import pi

def main():
    rospy.init_node('TUNE_AIRSPEED_THR', anonymous=True)
    command_topic = rospy.get_param('~command_topic', 'internal_commands')
    center_airspeed = rospy.get_param('~airspeed', 30.0)
    amplitude = rospy.get_param('~amplitude', 2)
    period = rospy.get_param('~period', 20)

    command_pub = rospy.Publisher(command_topic, Internal_Commands, queue_size=1)

    command = Internal_Commands()
    command.tuning_zone = 0 # TUNE_AIRSPEED_THR

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
