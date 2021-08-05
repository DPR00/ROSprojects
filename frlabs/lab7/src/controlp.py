#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from roslib import packages
import numpy as np

global x, y, w, t, ex, ey, ez
vel = np.array([0,0])
x=0; y=0; w=0; t=0
ex=0; ey=0; ez=0

valores = 0.1*np.array([2.3, 1, 1])
Kp = np.diag(valores)
xdes = np.array([3, 2, 1.57])

def callback(msg):
    global t, x, y, ex, ey, ez, w
    # Obtencion de datos
    t  = msg.header.stamp.secs        # tiempo
    x  = msg.pose.pose.position.x     # posicion x
    y  = msg.pose.pose.position.y     # posicion y
    ex = msg.pose.pose.orientation.x  # orientacion ex
    ey = msg.pose.pose.orientation.y  # orientacion ey
    ez = msg.pose.pose.orientation.z  # orientacion ez
    w = msg.pose.pose.orientation.w   # orientacion w

if __name__ == "__main__":
    rospy.init_node("info_circ")
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # Archivos donde se almacenara los datos
    fpose_act = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/frlabs/lab7/tmp/pose_actr.txt", "w")
    fpose_des = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/frlabs/lab7/tmp/pose_desr.txt", "w")
    # Frecuencia del envio (en Hz)
    freq = 20
    dt = 1.0/freq
    rate = rospy.Rate(freq)
    # Creamos un nodo subscriptor
    rospy.Subscriber('odom', Odometry, callback)

    while not rospy.is_shutdown():

        # Calculo del angulo de rotacion alrededor de z
        e = np.array([[ex,ey,ez]])      
        ang_z = 2*np.arctan2(np.linalg.norm(e),w)    
        print "Angulo de rotacion alrededor del eje z: "+ str(ang_z)
        print "Posiciones: " + str(x)+ ", " +str(y)

        # Almacenamiento de datos
        fpose_act.write(str(t)+' '+str(x)+' '+str(y)+' '+str(ang_z)+'\n')
        fpose_des.write(str(t)+' '+str(xdes[0])+' '+str(xdes[1])+' '+str(xdes[2])+'\n')

        xcur = np.array([x,y,ang_z])
        S = np.array([[np.cos(ang_z), 0],
                    [np.sin(ang_z), 0],
                    [0, 1]])
        S_ = np.linalg.inv((S.T).dot(S)).dot(S.T)
        vel = np.dot(S_,np.dot(Kp,xdes-xcur))
        twist = Twist()
        
        twist.linear.x = vel[0]; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = vel[1]
        
        if np.linalg.norm(xdes-x)<=0.01:
            break
        pub.publish(twist)

        rate.sleep()


    print "Ending motion ..."

    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)  

    fpose_act.close()
    fpose_des.close()
    print "Cerrado"