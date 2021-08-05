#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from roslib import packages
import numpy as np

global t, x, y, ex, ey, ez, w 
t=0; x= 0; y=0; ex=0; ey=0; ez= 0; w= 0

def callback_quat(msg):
    global t, x, y, ex, ey, ez, w 
    # Obtencion de datos
    t  = msg.header.stamp.secs        # tiempo
    x  = msg.pose.pose.position.x     # posicion x
    y  = msg.pose.pose.position.y     # posicion y
    ex = msg.pose.pose.orientation.x  # orientacion ex
    ey = msg.pose.pose.orientation.y  # orientacion ey
    ez = msg.pose.pose.orientation.z  # orientacion ez
    w = msg.pose.pose.orientation.w   # orientacion w
    

def Q2Matriz(w,e):
    '''
    w= Escalar del cuaternion unitario
    e= vector del cuaternion unitario
    '''
    ex=e[0,0]; ey=e[0,1]; ez=e[0,2]
    R=np.array([[2*(w**2+ex**2)-1, 2*(ex*ey-w*ez), 2*(ex*ez+ w*ey)],
                [2*(ex*ey+w*ez), 2*(w**2+ey**2)-1, 2*(ey*ez-w*ex)],
                [2*(ex*ez-w*ey), 2*(ey*ez+ w*ex), 2*(w**2 +ez**2)-1]])
    R=np.round(R,3)
    return R

if __name__ == "__main__":
    rospy.init_node("info_circ")
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # Archivos donde se almacenara los datos
    info_pose = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/frlabs/lab7/tmp/pose.txt", "w")
    # Definiciones
    r= 0.25; v=0.15
    # Creamos un nodo subscriptor
    rospy.Subscriber('odom', Odometry, callback_quat)
    try:
        while not rospy.is_shutdown():
            # Calculo del angulo de rotacion alrededor de z
            e = np.array([[ex,ey,ez]])      
            R = Q2Matriz(w, e)
            ang_z = np.arctan2(R[0,0],R[1,0])

            # Almacenamiento de datos
            info_pose.write(str(t)+' '+str(x)+' '+str(y)+' '+str(ang_z)+'\n')

            print "Angulo de rotacion alrededor del eje z: "+ str(ang_z)
            print "Posiciones: " + str(x)+ ", " +str(y)
            twist = Twist()

            twist.linear.x = v; twist.linear.y = 0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = v/r
            
            pub.publish(twist)
            
    except:
        print "Comunication Failed ..."

    finally:
        print "Ending motion ..."

        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)  

        info_pose.close()