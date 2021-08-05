import numpy as np

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

def Matriz_to_Q1(R):
    '''
    R= Matriz de rotación
    -------------------------------------------------------------------------------------------
    La función devuelve 1 lista con 2 elementos. El primero corresponde al valor del ángulo y el 2do al
    valor de "e", el cuál es un numpy.array(1,4)
    '''
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
    #w=np.round(w,3)
    Q=np.array([w, ex, ey, ez])
    return Q

def R2Q(R):
    w = 1.0/2.0*np.sqrt(1+R[0,0]+R[1,1]+R[2,2])
    epsx = 1.0/(4*w)*(R[2,1]-R[1,2])
    epsy = 1.0/(4*w)*(R[0,2]-R[2,0])
    epsz = 1.0/(4*w)*(R[1,0]-R[0,1])
    Q = np.array([w, epsx, epsy, epsz])
    
    return Q


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
        print(R[2,1]-R[1,2])
        quat[1] = 0.5*np.sign(R[2,1]-R[1,2])*np.sqrt(R[0,0]-R[1,1]-R[2,2]+1.0)
    if ( np.fabs(R[1,1]-R[2,2]-R[0,0]+1.0) < dEpsilon ):
        quat[2] = 0.0
    else:
        print(R[0,2]-R[2,0])
        quat[2] = 0.5*np.sign(R[0,2]-R[2,0])*np.sqrt(R[1,1]-R[2,2]-R[0,0]+1.0)
    if ( np.fabs(R[2,2]-R[0,0]-R[1,1]+1.0) < dEpsilon ):
        quat[3] = 0.0
    else:
        print(R[1,0]-R[0,1])
        quat[3] = 0.5*np.sign(R[1,0]-R[0,1])*np.sqrt(R[2,2]-R[0,0]-R[1,1]+1.0)

    return np.array(quat)

R = np.array([[0,1,0],[1,0,0],[0,0,-1]])
Q=Matriz_to_Q1(R)
Q_pf=rot2quat(R)
#Q_2=R2Q(R)
print(Q)
print(Q_pf)
#print(Q_2)
#print(np.shape(Q))
