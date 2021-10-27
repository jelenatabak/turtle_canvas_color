#!/usr/bin/env python3

import rospy

from turtlesim.msg import Pose, Color
from std_srvs.srv import Empty

class CanvasColor:
    def __init__(self):
        self.turtle_pose_sub = rospy.Subscriber("/turtle1/pose", Pose, self.turtlePoseCallback, queue_size=1)
        self.pose_flag = 1 # 1 if turtle is in the upper part of the screen, 0 otherwise

        rospy.wait_for_service('clear')
        self.clear_srv = rospy.ServiceProxy('clear', Empty)
        rospy.spin()

    def turtlePoseCallback(self, msg):
        if self.pose_flag and msg.y < 5.4:
            rospy.set_param('/turtlesim/background_r', 255)
            rospy.set_param('/turtlesim/background_b', 0)
            self.pose_flag = 0
            self.clear_srv()


        elif not self.pose_flag and msg.y > 5.4:
            rospy.set_param('/turtlesim/background_r', 0)
            rospy.set_param('/turtlesim/background_b', 255)
            self.pose_flag = 1
            self.clear_srv()

def main():
  rospy.init_node('turtle_canvas_color', anonymous=True)
  canvas_color = CanvasColor()


if __name__ == '__main__':
    main()
