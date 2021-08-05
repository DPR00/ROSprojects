import numpy as np
from copy import copy

pi = np.pi


def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.

    """
    sth = np.sin(theta)
    cth = np.cos(theta)
    sa  = np.sin(alpha)
    ca  = np.cos(alpha)
    T = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                  [sth,  ca*cth, -sa*cth, a*sth],
                  [0.0,      sa,      ca,     d],
                  [0.0,     0.0,     0.0,   1.0]])
    return T


def fkine(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]

    """
    # Longitudes (en metros)
    c =0.001
    # Matrices DH (completar), emplear la funcion dh con los parametros DH para cada articulacion
    #d =np.array([89.159*c, 0, 0, 109.15*c, 94.65*c, 82.3*c])
    #th=np.array([0, 0, 0, 0, 0, 0])
    #a =np.array([0, -425*c, -392.25*c, 0, 0, 0])
    #alpha = np.array([pi/2, 0, 0, pi/2, -pi/2, 0])
    d =np.array([89.2*c, 109.3*c, -109.3*c, 109.3*c, 94.75*c, 82.5*c])
    th=np.array([0, np.pi, 0, np.pi, np.pi, 0])
    a =np.array([0, 425*c, 392*c, 0, 0, 0])
    alpha = np.array([np.pi/2, 0, 0, np.pi/2, np.pi/2, np.pi])

    T1 = dh(d[0],  q[0]+th[0], a[0], alpha[0])
    T2 = dh(d[1],  q[1]+th[1], a[1], alpha[1])
    T3 = dh(d[2],  q[2]+th[2], a[2], alpha[2])
    T4 = dh(d[3],  q[3]+th[3], a[3], alpha[3])
    T5 = dh(d[4],  q[4]+th[4], a[4], alpha[4])
    T6 = dh(d[5],  q[5]+th[5], a[5], alpha[5])
    # Efector final con respecto a la base
    T = T1.dot(T2).dot(T3).dot(T4).dot(T5).dot(T6)
    return T


def jacobian_position(q, delta=0.0001):
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


def jacobian_pose(q, delta=0.0001):
    """
    Jacobiano analitico para la posicion y orientacion (usando un
    cuaternion). Retorna una matriz de 7x6 y toma como entrada el vector de
    configuracion articular q=[q1, q2, q3, q4, q5, q6]

    """
    # Crear una matriz de 7x6 para la alocacion de memoria
    J = np.zeros((7,6))
    # Transformacion homogenea inicial (usando q)
    T0=fkine(q)
    pose_inicial=TF2xyzquat(T0)

    for i in xrange(6):
        # Copiar la configuracion articular inicial
        dq = copy(q)
        # Incrementar la articulacion i-esima usando un delta
        dq[i]= dq[i]+delta
        # Transformacion homogenea (TH) luego del incremento (q+delta)
        T_inc= fkine(dq)
        # Pose of the robot from TH
        pose=TF2xyzquat(T_inc)
        # Aproximacion del Jacobiano de la tarea usando diferencias finitas
        J[0:7,i]=(pose-pose_inicial)/delta
   
    return J



def rot2quat(R):
    """
    Convertir una matriz de rotacion en un cuaternion

    Entrada:
      R -- Matriz de rotacion
    Salida:
      Q -- Cuaternion [ew, ex, ey, ez]

    """
    
    dEpsilon = 1e-6
    quat = 4*[0.,]

    quat[0] = 0.5*np.sqrt(R[0,0]+R[1,1]+R[2,2]+1.0)
    if ( np.fabs(R[0,0]-R[1,1]-R[2,2]+1.0) < dEpsilon ):
        quat[1] = 0.0
    else:
        quat[1] = 0.5*np.sign(R[2,1]-R[1,2])*np.sqrt(R[0,0]-R[1,1]-R[2,2]+1.0)
    if ( np.fabs(R[1,1]-R[2,2]-R[0,0]+1.0) < dEpsilon ):
        quat[2] = 0.0
    else:
        quat[2] = 0.5*np.sign(R[0,2]-R[2,0])*np.sqrt(R[1,1]-R[2,2]-R[0,0]+1.0)
    if ( np.fabs(R[2,2]-R[0,0]-R[1,1]+1.0) < dEpsilon ):
        quat[3] = 0.0
    else:
        quat[3] = 0.5*np.sign(R[1,0]-R[0,1])*np.sqrt(R[2,2]-R[0,0]-R[1,1]+1.0)

    return np.array(quat)
    
    """
    r11=R[0,0]; r12=R[0,1]; r13=R[0,2];
    r21=R[1,0]; r22=R[1,1]; r23=R[1,2];
    r31=R[2,0]; r32=R[2,1]; r33=R[2,2];
    w=0.5*np.sqrt(1+r11+r22+r33)
    e=np.array([[0, 0, 0]]);
    if np.round(w,3)==0:
        print("W==0, checkear")
        ex=0.5*np.sqrt(1+r11-r22-r33)
        ey=0.5*np.sqrt(1-r11+r22-r33)
        ez=0.5*np.sqrt(1-r11-r22+r33)
        
        if ex>ey:
            if ex>ez:
                ey=0.25*(r12+r21)/ex
                ez=0.25*(r13+r31)/ex
            else:
                ey=0.25*(r23+r32)/ez
                ex=0.25*(r13+r31)/ez
        else:
            if ey>ez:
                ez=0.25*(r23+r32)/ey
                ex=0.25*(r12+r21)/ey
            else:
                ey=0.25*(r23+r32)/ez
                ex=0.25*(r13+r31)/ez 
        
    else:
        ex=(r32-r23)/(4*w)
        ey=(r13-r31)/(4*w)
        ez=(r21-r12)/(4*w)
    w=np.round(w,5)
    Q=np.array([w, np.round(ex,5), np.round(ey,5), np.round(ez,5)])
    
    return Q
    """

def TF2xyzquat(T):
    """
    Convert a homogeneous transformation matrix into the a vector containing the
    pose of the robot.

    Input:
      T -- A homogeneous transformation
    Output:
      X -- A pose vector in the format [x y z ew ex ey ez], donde la first part
           is Cartesian coordinates and the last part is a quaternion
    """
    quat = rot2quat(T[0:3,0:3])
    res = [T[0,3], T[1,3], T[2,3], quat[0], quat[1], quat[2], quat[3]]
    return np.array(res)


def skew(w):
    R = np.zeros([3,3])
    R[0,1] = -w[2]; R[0,2] = w[1]
    R[1,0] = w[2];  R[1,2] = -w[0]
    R[2,0] = -w[1]; R[2,1] = w[0]
    return R
