#!/usr/bin/env python
import os
import rospy
from duckietown import DTROS
from std_msgs.msg import String
from duckietown_msgs.msg import BoolStamped



class lane_recovery(object):

    def __init__(self):
        self.node_name = rospy.get_name()
        self.pub_car_cmd = rospy.Publisher("~rescue_on", BoolStamped, queue_size=1)
        self.rescue_on = BoolStamped()
        self.rescue_on.data = False

    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(1) # 1Hz

        while not rospy.is_shutdown():
            trigger = rospy.get_param("~trigger_rescue")
            print(trigger)
            rate.sleep()

if __name__ == '__main__':
    #will execute, if this is called as a main file
    # create the node

    rospy.init_node("lane_recovery_node", anonymous=False)  # adapted to sonjas default file
    lane_recovery_node = lane_recovery()
    lane_recovery_node.run()
    # keep spinning
    rospy.spin()
