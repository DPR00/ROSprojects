#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:34:27 2021

@author: diegopalma
"""

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import axes3d

print("Loading data from files...")

xcurrent = open("xcurrent_diffk.txt", 'r')
xdesired = open("xdesired_diffk.txt", 'r') 
q= open("q_diffk.txt",'r')

xc_x=np.array([]); xc_y=np.array([]); xc_z=np.array([])
xd_x=np.array([]); xd_y=np.array([]); xd_z=np.array([])
q0=np.array([]); q1=np.array([]); q2=np.array([])
q3=np.array([]); q4=np.array([]); q5=np.array([])
freq = 200
dt = 1.0/freq

# Leer Datos de los valores actuales
for line in xcurrent:
    line = xcurrent.readline()
    xyz=line.split()
    try:
        x=float(xyz[0]); xc_x=np.append(xc_x, x)
        y=float(xyz[1]); xc_y=np.append(xc_y, y)
        z=float(xyz[2]); xc_z=np.append(xc_z, z)
    except:
        pass

# Leer Datos de los valores deseados
for line in xdesired:
    line = xdesired.readline()
    xyz=line.split()
    try:
        x=float(xyz[0]); xd_x=np.append(xd_x, x)
        y=float(xyz[1]); xd_y=np.append(xd_y, y)
        z=float(xyz[2]); xd_z=np.append(xd_z, z)
    except:
        pass

for line in q:
    line = q.readline()
    xyz=line.split()
    try:
        q_0=float(xyz[0]); q0=np.append(q0, q_0)
        q_1=float(xyz[1]); q1=np.append(q1, q_1)
        q_2=float(xyz[2]); q2=np.append(q2, q_2)
        q_3=float(xyz[3]); q3=np.append(q3, q_3)
        q_4=float(xyz[4]); q4=np.append(q4, q_4)
        q_5=float(xyz[5]); q5=np.append(q5, q_5)
    except:
        pass
    
# %% Posiciones articulares
total=len(q0)
tiempo=dt*np.arange(0,total)

#fig, axs = plt.subplots(2,2)

fig= plt.figure(figsize=(20,9))

fig.suptitle("Configuraciones articulares", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(231)
axs1=plt.subplot(232)
axs2=plt.subplot(233)
axs3=plt.subplot(234)
axs4=plt.subplot(235)
axs5=plt.subplot(236)

axs0.plot(tiempo, q0[0:total], color="blue", label= "Configuración articular 0")
axs0.set(xlabel='Tiempo (s)', ylabel='Configuración articular 0 (rad)')
axs0.set_title('q0 vs tiempo')
axs0.legend()

axs1.plot(tiempo, q1[0:total], color="blue", label= "Configuración articular 1")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Configuración articular 1 (rad)')
axs1.set_title('q1 vs tiempo')
axs1.legend()

axs2.plot(tiempo, q2[0:total], color="blue", label= "Configuración articular 2")
axs2.set(xlabel='Tiempo (s)', ylabel='Configuración articular 2 (rad)')
axs2.set_title('q2 vs tiempo')
axs2.legend()

axs3.plot(tiempo, q3[0:total], color="blue", label= "Configuración articular 3")
axs3.set(xlabel='Tiempo (s)', ylabel='Configuración articular 3 (rad)')
axs3.set_title('q3 vs tiempo')
axs3.legend()

axs4.plot(tiempo, q4[0:total], color="blue", label= "Configuración articular 4")
axs4.set(xlabel= 'Tiempo (s)', ylabel='Configuración articular 4 (rad)')
axs4.set_title('q4 vs tiempo')
axs4.legend()

axs5.plot(tiempo, q5[0:total], color="blue", label= "Configuración articular 5")
axs5.set(xlabel='Tiempo (s)', ylabel='Configuración articular 5 (rad)')
axs5.set_title('q5 vs tiempo')
axs5.legend()

# %% Posiciones cartesianas

total=len(xc_x)
tiempo=dt*np.arange(0,total)

#fig, axs = plt.subplots(2,2)

fig= plt.figure(figsize=(12,9))

fig.suptitle("Posiciones cartesianas", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(221)
axs1=plt.subplot(222)
axs2=plt.subplot(212)

axs0.plot(tiempo, xc_x[0:total], color="blue", label= "Posición actual de x")
axs0.plot(tiempo, xd_x[0:total], color="green", label= "Posición deseada de x")
axs0.set(xlabel='Tiempo (s)', ylabel='Posición en x (m)')
axs0.set_title('Posición en X vs tiempo')
axs0.legend()

axs1.plot(tiempo, xc_y[0:total], color="blue", label= "Posición actual de y")
axs1.plot(tiempo, xd_y[0:total], color="green", label= "Posición deseada de y")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Posición en y (m)')
axs1.set_title('Posición en Y vs tiempo')
axs1.legend()

axs2.plot(tiempo, xc_z[0:total], color="blue", label= "Posición actual de z")
axs2.plot(tiempo, xd_z[0:total], color="green", label= "Posición deseada de z")
axs2.set(xlabel='Tiempo (s)', ylabel='Posición en y (m)')
axs2.set_title('Posición en Z vs tiempo')
axs2.legend()

# %% ERROR
fig= plt.figure(figsize=(12,9))
fig.suptitle("Error", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(221)
axs1=plt.subplot(222)
axs2=plt.subplot(212)
axs0.plot(tiempo, np.abs(xc_x[0:total]-xd_x[0:total]), color="blue", label= "Posición actual de x")
axs0.plot(tiempo, np.zeros(total), color="green", label= "Posición deseada de x")
axs0.set(xlabel='Tiempo (s)', ylabel='Error en x (m)')
axs0.set_title('Error en X vs tiempo')
axs0.legend()

axs1.plot(tiempo, np.abs(xc_y[0:total]-xd_y[0:total]), color="blue", label= "Posición actual de y")
axs1.plot(tiempo, np.zeros(total), color="green", label= "Posición deseada de y")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Error en y (m)')
axs1.set_title('Error en Y vs tiempo')
axs1.legend()

axs2.plot(tiempo, np.abs(xc_z[0:total]-xd_z[0:total]), color="blue", label= "Posición actual de z")
axs2.plot(tiempo, np.zeros(total), color="green", label= "Posición deseada de z")
axs2.set(xlabel='Tiempo (s)', ylabel='Error en y (m)')
axs2.set_title('Error en Z vs tiempo')
plt.show()

# %% Creamos la figura 3D
"""
fig = plt.figure(figsize=(12,10))

# Agrrgamos un plano 3D
ax_3d = fig.add_subplot(projection='3d')

# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
xcx=xc_x[0:total]
xcy=xc_y[0:total]
xcz=xc_z[0:total]
xcx=np.reshape(xcx,(1,len(xcx)))
xcy=np.reshape(xcy,(1,len(xcy)))
xcz=np.reshape(xcz,(1,len(xcz)))
ax_3d.plot_wireframe(xcx, xcy, xcz, color='blue', linewidth=4)
ax_3d.scatter(xcx[0,0], xcy[0,0], xcz[0,0], color='red', linewidth=12, marker='o')
ax_3d.scatter(xcx[0,total-1], xcy[0,total-1], xcz[0,total-1], color='green', linewidth=12, marker='o')
ax_3d.set(xlabel="Posición en X (m)", ylabel="Posición en Y (m)", zlabel="Posición en Z (m)")
ax_3d.set_title("Espacio cartesiano", fontsize=22)
# Mostramos el gráfico
plt.show()
"""
