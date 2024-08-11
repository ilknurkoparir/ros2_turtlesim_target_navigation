#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys


#class and function
class VelController(Node):
    def __init__(self):
        super().__init__("vel_controller_name")
        self.publishers_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer = self.create_timer(1,self.publish_vel)
        self.get_logger().info("Velocity Controller has been published")
    
    def publish_vel(self):
        msg = Twist()
        """
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        #Robotu döndürmek için kullanılır.
        msg.angular.z = 0.5 #-3.14 & +3.14

        """

        linear_x = float(sys.argv[1])
        radius = float(sys.argv[2])

        msg.linear.x = linear_x
        msg.linear.y = 0.0
        msg.angular.z  = float(linear_x/radius)
   

        self.publishers_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = VelController()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__  == "__main__":
    main()








