import rbdl
import numpy as np


# Lectura del modelo del robot a partir de URDF (parsing)
modelo = rbdl.loadModel('../urdf/ur5_robot.urdf')
# Grados de libertad
ndof = modelo.q_size

# Configuracion articular
q = np.array([0.5, 0.2, 0.3, 0.8, 0.5, 0.6])
# Velocidad articular
dq = np.array([0.8, 0.7, 0.8, 0.6, 0.9, 1.0])
# Aceleracion articular
ddq = np.array([0.2, 0.5, 0.4, 0.3, 1.0, 0.5])

# Arrays numpy
zeros = np.zeros(ndof)          # Vector de ceros
tau   = np.zeros(ndof)          # Para torque
g     = np.zeros(ndof)          # Para la gravedad
c     = np.zeros(ndof)          # Para el vector de Coriolis+centrifuga
M     = np.zeros([ndof, ndof])  # Para la matriz de inercia
e     = np.eye(6)               # Vector identidad

# Torque dada la configuracion del robot
rbdl.InverseDynamics(modelo, q, dq, ddq, tau)

# Parte 1: Calcular vector de gravedad, vector de Coriolis/centrifuga,
# y matriz M usando solamente InverseDynamics

# Vector de gravedad
rbdl.InverseDynamics(modelo, q, np.zeros(ndof), np.zeros(ndof), g)
print "Vector de gravedad: " + str(np.round(g,4))
# Vector de Coriolis/centrifuga
rbdl.InverseDynamics(modelo, q, dq, np.zeros(ndof), c)
c = c - g
print "Vector de Coriolis/centrifuga: "+ str(np.round(c,4))
# Matriz M
mi=np.zeros(ndof)
for i in range(ndof):
    ei=e[i,:]
    rbdl.InverseDynamics(modelo, q, np.zeros(ndof), ei, mi)
    M[:, i]= mi - g 
print "Matriz de inercia:\n"+str(np.round(M,4))

# Parte 2: Calcular M y los efectos no lineales b usando las funciones
# CompositeRigidBodyAlgorithm y NonlinearEffects. Almacenar los resultados
# en los arreglos llamados M2 y b2
b2 = np.zeros(ndof)          # Para efectos no lineales
M2 = np.zeros([ndof, ndof])  # Para matriz de inercia

# Calculando la Matriz de inercia
rbdl.CompositeRigidBodyAlgorithm(modelo, q, M2)
print "Matriz de inercia:\n"+ str(np.round(M2,4))

# Calculando la matriz de efectos no lineales
rbdl.NonlinearEffects(modelo, q, dq, b2)
print  "Efectos no lineales: " + str(np.round(b2,4))

# Parte 2: Verificacion de valores
print "\nParte 2: Verificacion de valores\n"
# Verificar Matriz M
val_M = False
if (M2.all() == M.all()):
    val_M = True
    
print "Las Matrices M2 y M son iguales: " + str(val_M)
print "La diferencia entre cada elemento es: "
print M2-M

print "\n"
# Verificar vecto b
val_b = False
b= c+g
if (b2.all() == b.all()):
    val_b = True
    
print "El vector b2 es igual a la suma de c y g: " + str(val_b)
print "La diferencia entre cada elemento es: "
print b2-b

# Parte 3: Verificacion de la expresion de la dinamica
# Matriz de inercia
M_ddq= np.dot(M,ddq)
print "\nPrimer termino: "
print M_ddq

# Fuerzas de coriolis y vector de gravedad
cg= c+g
print " Segundo y tercer termino: "
print cg

## Todo el termino de la izquirda
TI = M_ddq+cg
print "Termino de la izquierda"
print TI

## Termino de la derecha
print "Termino de la derecha"
print tau

if (TI.all() == tau.all() ):
    print "Modelo calculado correctamente!"
else:
    print "Falla en el calculo :("

