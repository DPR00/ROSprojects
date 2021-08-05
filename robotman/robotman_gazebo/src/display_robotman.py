#!/usr/bin/env python

import cv2
import rospy
import rospkg
import cv_bridge
from sensor_msgs.msg import Image

if __name__ == '__main__':
    
  rospy.init_node("display_robotman")

  rospack = rospkg.RosPack()
  image_path = rospack.get_path('robotman_gazebo') + '/images/'
  img = cv2.imread(image_path + 'screen.png')

  msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
  pub = rospy.Publisher('/screen/body/image', Image, latch=True, queue_size=1)
  rate = rospy.Rate(1)

  while not rospy.is_shutdown():

    pub.publish(msg)
    rate.sleep()

