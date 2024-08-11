#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToLocationNode(Node):
    def __init__(self):
        super().__init__("go_to_loc_node")


        self.target_x = 2.0 # 0.0 - 11.0 , Default location_x ~ 5.5
        self.target_y = 8.0 # 0.0 - 11.0 .  Default location_y ~ 5.5

        self.publisher_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.subscriber_ = self.create_subscription(Pose,"/turtle1/pose",self.callback_turtle_pose,10)

        self.timer = self.create_timer(1.0,self.turtle_controller)
        self.get_logger().info("Navigating to target location !")


    def callback_turtle_pose(self,msg):
        self.pose_ = msg

    def turtle_controller(self):
        msg = Twist()
        distance_x = self.target_x - self.pose_.x
        distance_y = self.target_y - self.pose_.y


        distance = math.sqrt(distance_x**2 + distance_y**2)
        target_theta = math.atan2(distance_y,distance_x)

        if abs(target_theta - self.pose_.theta) > 0.1:
            msg.angular.z = target_theta - self.pose_.theta

        else:
            if distance >= 0.1 :
                msg.linear.x = distance 

            else:
                msg.linear.x = 0.0    

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = GoToLocationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()