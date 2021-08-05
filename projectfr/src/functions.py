import numpy as np
from copy import copy
import rbdl 

cos=np.cos; sin=np.sin; pi=np.pi

class Robot(object):
    def __init__(self, q0, dq0, ndof, dt):
        self.q = q0    # numpy array (ndof x 1)
        self.dq = dq0  # numpy array (ndof x 1)
        self.M = np.zeros([ndof, ndof])
        self.b = np.zeros(ndof)
        self.dt = dt
        self.robot = rbdl.loadModel('/home/diegopalma/Documents/ROSProjects/lab_ws/src/projectfr/urdf/robotfr.urdf')

    def send_command(self, tau):
        rbdl.CompositeRigidBodyAlgorithm(self.robot, self.q, self.M)
        rbdl.NonlinearEffects(self.robot, self.q, self.dq, self.b)
        ddq = np.linalg.inv(self.M).dot(tau-self.b)
        self.q = self.q + self.dt*self.dq
        self.dq = self.dq + self.dt*ddq

    def read_joint_positions(self):
        return self.q

    def read_joint_velocities(self):
        return self.dq
    def read_M(self):
        return self.M
    def read_b(self):
        return self.b

def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.
    """
    # Escriba aqui la matriz de transformacion homogenea en funcion de los valores de d, theta, a, alpha
    cth= np.cos(theta); sth=np.sin(theta)
    ca = np.cos(alpha); sa=np.sin(alpha)

    T = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                  [sth,  ca*cth, -sa*cth, a*sth],
                  [  0,      sa,      ca,     d],
                  [  0,       0,       0,     1]])    
    return T
    
def fkine(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]
    """
    # Longitudes (en metros)
    m=0.001
    a_= 32*m; b_= 127*m; c_= 108*m 
    d_= 20*m; e_= 169*m; f_= 70*m
    # Matrices DH (completar), emplear la funcion dh con los parametros DH para cada articulacion
    d =np.array([b_, 0, 0, e_, 0, -f_])
    th=np.array([pi, pi/2, pi, pi, pi/2, 0])
    a =np.array([-a_, c_, -d_, 0, 0, 0])
    alpha = np.array([pi/2, 0, pi/2, pi/2, pi/2, pi])
    
    T1 = dh(d[0],  q[0]+th[0], a[0], alpha[0])
    T2 = dh(d[1],  q[1]+th[1], a[1], alpha[1])
    T3 = dh(d[2],  q[2]+th[2], a[2], alpha[2])
    T4 = dh(d[3],  q[3]+th[3], a[3], alpha[3])
    T5 = dh(d[4],  q[4]+th[4], a[4], alpha[4])
    T6 = dh(d[5],  q[5]+th[5], a[5], alpha[5])

    # Efector final con respecto a la base
    T = T1.dot(T2).dot(T3).dot(T4).dot(T5).dot(T6)
    return T

def jacobian(q, delta=0.0001):
    """
    Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]
    """
    # Crear una matriz 3x6 para la alocacion de memoria
    J = np.zeros((3,6))
    # Transformacion homogenea inicial (usando q)
    T0=fkine(q)
    
    # Iteracion para la derivada de cada columna
    for i in xrange(6):
        # Copiar la configuracion articular inicial
        dq = copy(q)
        # Incrementar la articulacion i-esima usando un delta
        dq[i]=dq[i]+delta
        # Transformacion homogenea luego del incremento (q+delta)
        T_inc=fkine(dq)
        # Aproximacion del Jacobiano de posicion usando diferencias finitas
        J[0:3,i]=(T_inc[0:3,3]-T0[0:3,3])/delta
    return J

def ikine(xdes, q0):
    """
    Calcular la cinematica inversa de UR5 numericamente a partir de la configuracion articular inicial de q0. 
    """
    epsilon  = 0.0001
    max_iter = 5000
    delta    = 0.00001
    
    q  = copy(q0)
    for i in range(max_iter):
        # Main loop
        J=jacobian(q,delta)
        T=fkine(q)
        f=T[0:3,3]
        e= xdes-f
        q=q+np.dot(np.linalg.pinv(J),e)
        # Condicion de termino
        if (np.linalg.norm(e) < epsilon):
            break
    return q
