#!/usr/bin/env python

import rospy
import cv2
import cv_bridge
from sensor_msgs.msg import Image

if __name__ == '__main__':
    
  rospy.init_node("display_robotman")
  img = cv2.imread('screen.png')
  msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
  pub = rospy.Publisher('/screen/body/image', Image, latch=True, queue_size=1)
  rate = rospy.Rate(2)

  while not rospy.is_shutdown():

    pub.publish(msg)
    rate.sleep()

