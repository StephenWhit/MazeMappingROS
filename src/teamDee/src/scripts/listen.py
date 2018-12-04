#!/usr/bin/env python
import rospy
import roslib; roslib.load_manifest('laser')
from sensor_msgs.msg import LaserScan
import numpy as np
import amcl

def callback(data):
    pass
def laser_listener():
    pass
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber("/sensor_msgs/LaserScan",sensor_msgs.msg.LaserScan,callback,20)
    rospy.spin()

    

if __name__ == '__main__':
    laser_listener()

