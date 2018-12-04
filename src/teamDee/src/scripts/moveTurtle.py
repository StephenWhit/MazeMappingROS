#!/usr/bin/env python
# license removed for brevity
import rospy
import navRRT

from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

def Move_Turtle():
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.init_node('Move_Turtle', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    global msg
    msg = Twist()
    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    rrt = RRT(start=[0, 0], goal=[5, 10],
              randArea=[-2, 15], obstacleList=[0,0,0])
    path = rrt.Planning(animation=show_animation)


    while not rospy.is_shutdown():
        while not rospy.is_shutdown():
        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in a specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(msg)
            #Takes actual time to velocity calculus
            t1 = rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance = speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        Move_Turtle()

    except rospy.ROSInterruptException:
        pass
