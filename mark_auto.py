#!/usr/bin/env python
import rospy
from sys import argv

from rosflight_msgs.msg import Status


class AutoChecker:
    def main(self):
        rospy.init_node("mark_auto", anonymous=True)
        status_sub = rospy.Subscriber('/status', Status, self.status_cb)
        self.last_override = False
        self.last_offboard = False
        rospy.spin()

    def status_cb(self, status):
        if status.rc_override != self.last_override:
            print("RC Override %s: %f" % ("On" if status.rc_override else "Off", status.header.stamp.secs))
            self.last_override = status.rc_override
        if status.offboard != self.last_offboard:
            print("Offboard %s: %f" % ("On" if status.offboard else "Off", status.header.stamp.secs))
            self.last_offboard = status.offboard


if __name__=="__main__":
    AutoChecker().main()
