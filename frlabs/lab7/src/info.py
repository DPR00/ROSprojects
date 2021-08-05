#!/usr/bin/env python

import rospy
from geometry_msgs.msg import *
from nav_msgs.msg import Odometry
from roslib import packages
import numpy as np

def callback_quat(msg):
    # Obtencion de datos
    t  = msg.header.stamp.secs        # tiempo
    x  = msg.pose.pose.position.x     # posicion x
    y  = msg.pose.pose.position.y     # posicion y
    z  = msg.pose.pose.position.z     # posicion z
    ex = msg.pose.pose.orientation.x  # orientacion ex
    ey = msg.pose.pose.orientation.y  # orientacion ey
    ez = msg.pose.pose.orientation.z  # orientacion ez
    w = msg.pose.pose.orientation.w   # orientacion w
    
    # Calculo del angulo de rotacion alrededor de z
    e = np.array([[ex,ey,ez]])      
    R = Q2Matriz(w, e)
    ang_z = np.arctan2(R[1,0],R[0,0])

    # Almacenamiento de datos
    info_pose.write(str(t)+' '+str(x)+' '+str(y)+' '+str(ang_z)+'\n')

    print "Angulo de rotacion alrededor del eje z: "+ str(ang_z)
    print "Posiciones: " + str(x)+ ", " +str(y) + "," +str(z)


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
    rospy.init_node("info_node_pose")
    
    # Archivos donde se almacenara los datos
    info_pose = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/frlabs/lab7/tmp/pose.txt", "w")
    # Creamos un nodo subscriptor
    rospy.Subscriber('odom', Odometry, callback_quat)

    rospy.spin()

    print "End motion ..."
    info_pose.close()