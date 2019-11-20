#!/usr/bin/env python
import os
import rospy
from duckietown import DTROS
from std_msgs.msg import String
from duckietown_msgs.msg import BoolStamped



class rescue_trigger(object):

    def __init__(self):
        self.node_name = rospy.get_name()
        self.pub_trigger = rospy.Publisher("/autobot27/recovery_on", BoolStamped, queue_size=1)
        # self.pub_trigger = rospy.Publisher("/autobot27/recovery_off", BoolStamped, queue_size=1)


        self.rescue_on = BoolStamped
        self.rescue_on.Data = False
        self.rescue_off = BoolStamped
        self.rescue_off.Data = True


    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(1) # 1Hz

        while not rospy.is_shutdown():
            trigger = rospy.get_param("~trigger_rescue")
            if trigger != self.rescue_on.Data:
                self.rescue_on.Data = trigger
                self.rescue_off.Data = not trigger
                print("[rescue_trigger_node]: changed rescue_on to %s"%trigger)
                self.pub_trigger.publish(self.rescue_on)
            rate.sleep()

if __name__ == '__main__':
    #will execute, if this is called as a main file
    # create the node

    rospy.init_node("rescue_trigger_node", anonymous=False)  # adapted to sonjas default file
    rescue_trigger_node = rescue_trigger()
    rescue_trigger_node.run()
    # keep spinning
    rospy.spin()
