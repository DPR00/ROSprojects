#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from markers import *
from functions import *
from roslib import packages
import rbdl

rospy.init_node("control_pdg")
pub = rospy.Publisher('joint_states', JointState, queue_size=1000)
bmarker_actual  = BallMarker(color['RED'])
bmarker_deseado = BallMarker(color['GREEN'])
# Archivos donde se almacenara los datos
fqact = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/tmp/qactual_pdg.txt", "w")
fqdes = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/tmp/qdeseado_pdg.txt", "w")
fxact = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/tmp/xactual_pdg.txt", "w")
fxdes = open("/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/tmp/xdeseado_pdg.txt", "w")

# Nombres de las articulaciones
jnames = ['joint1', 'joint2', 'joint3',
          'joint4', 'joint5', 'joint6']
# Objeto (mensaje) de tipo JointState
jstate = JointState()
# Valores del mensaje
jstate.header.stamp = rospy.Time.now()
jstate.name = jnames

# =============================================================
# Configuracion articular inicial (en radianes)
q = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Velocidad inicial
dq = np.array([0., 0., 0., 0., 0., 0.])
# Configuracion articular deseada
qdes = np.array([-2.26,  0.086, -0.26, -1.39, -0.55,  0.0])
# =============================================================

# Posicion resultante de la configuracion articular deseada
xdes = fkine(qdes)[0:3,3]
# Copiar la configuracion articular en el mensaje a ser publicado
jstate.position = q
pub.publish(jstate)

# Modelo RBDL
modelo = rbdl.loadModel('/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/urdf/robotfr.urdf')
ndof   = modelo.q_size     # Grados de libertad

# Frecuencia del envio (en Hz)
freq = 20
dt = 1.0/freq
rate = rospy.Rate(freq)

# Simulador dinamico del robot
robot = Robot(q, dq, ndof, dt)

# Se definen las ganancias del controlador
#valores = 0.1*np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
valores = 1*np.array([5, 5, 5, 5, 5, 5])
Kp = np.diag(valores)
Kd = 2*np.sqrt(Kp)
g = np.zeros(ndof)

# Bucle de ejecucion continua
t = 0.0
while not rospy.is_shutdown():

    # Leer valores del simulador
    q  = robot.read_joint_positions()
    dq = robot.read_joint_velocities()
    # Posicion actual del efector final
    x = fkine(q)[0:3,3]
    # Tiempo actual (necesario como indicador para ROS)
    jstate.header.stamp = rospy.Time.now()

    # Almacenamiento de datos
    fxact.write(str(t)+' '+str(x[0])+' '+str(x[1])+' '+str(x[2])+'\n')
    fxdes.write(str(t)+' '+str(xdes[0])+' '+str(xdes[1])+' '+
                str(xdes[2])+'\n')
    fqact.write(str(t)+' '+str(q[0])+' '+str(q[1])+' '+ str(q[2])+
                ' '+ str(q[3])+' '+str(q[4])+' '+str(q[5])+'\n ')
    fqdes.write(str(t)+' '+str(qdes[0])+' '+str(qdes[1])+' '+ str(qdes[2])+
                ' '+ str(qdes[3])+' '+str(qdes[4])+' '+str(qdes[5])+'\n ')

    # ----------------------------
    # Control dinamico 
    # ----------------------------
    rbdl.InverseDynamics(modelo, q, np.zeros(ndof), np.zeros(ndof), g)
    ST = Kp.dot(qdes-q)
    TT = -Kd.dot(dq)
    u = g + ST + TT   # Ley de control
    if np.linalg.norm(qdes-q)<0.01:
        break

    # Simulacion del robot
    robot.send_command(u)

    # Publicacion del mensaje
    jstate.position = q
    pub.publish(jstate)
    bmarker_deseado.xyz(xdes)
    bmarker_actual.xyz(x)
    t = t+dt
    # Esperar hasta la siguiente  iteracion
    rate.sleep()

print "End motion ..."
fqact.close()
fqdes.close()
fxact.close()
fxdes.close()