#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:45:25 2021

@author: diegopalma
"""

# drift
import numpy as np
import matplotlib.pyplot as plt

print("Loading data from files...")

pose_act = open("pose_actr.txt", 'r')
pose_des = open("pose_desr.txt", 'r')

# Pose
timec=np.array([]); xc=np.array([]); yc=np.array([]); ang_zc=np.array([])
timed=np.array([]); xd=np.array([]); yd=np.array([]); ang_zd=np.array([])

# Leer Datos de los valores actuales
for line in pose_act:
    line = pose_act.readline()
    xyz=line.split()
    try:
        t_=float(xyz[0]); timec=np.append(timec, t_)
        x_=float(xyz[1]); xc=np.append(xc, x_)
        y_=float(xyz[2]); yc=np.append(yc, y_)
        z_=float(xyz[3]); ang_zc=np.append(ang_zc, z_)
    except:
        pass
    
for line in pose_des:
    line = pose_des.readline()
    xyz=line.split()
    try:
        t_=float(xyz[0]); timed=np.append(timed, t_)
        x_=float(xyz[1]); xd=np.append(xd, x_)
        y_=float(xyz[2]); yd=np.append(yd, y_)
        z_=float(xyz[3]); ang_zd=np.append(ang_zd, z_)
    except:
        pass
    
step = (max(timec)-min(timec))/len(timec)
leng = len(timec)
stop = max(timec)-min(timec)
time = np.arange(0, stop, step)
time = time[0:leng]
# %%

total= len(time)
#fig, axs = plt.subplots(2,2)
fig= plt.figure(figsize=(16,10))

fig.suptitle("Pose", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(221)
axs1=plt.subplot(222)
axs2=plt.subplot(212)

axs0.plot(time[0:total], xc[0:total], color="blue", label= "Posición en X actual")
axs0.plot(time[0:total], xd[0:total], color="green", label= "Posición en X deseado")
axs0.set(xlabel='Tiempo (s)', ylabel='Posición en x (m)')
axs0.set_title('Posición en x vs tiempo')
axs0.legend()

axs1.plot(time[0:total], yc[0:total], color="blue", label= "Posición en Y actual")
axs1.plot(time[0:total], yd[0:total], color="green", label= "Posición en Y deseado")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Posición en Y (m)')
axs1.set_title('Posición en y vs tiempo')
axs1.legend()

axs2.plot(time[0:total], ang_zc[0:total], color="blue", label= "Ángulo de orientaicón actual")
axs2.plot(time[0:total], ang_zd[0:total], color="green", label= "Ángulo de orientaicón deseado")
axs2.set(xlabel='Tiempo (s)', ylabel='Ángulo de orientación (rad)')
axs2.set_title('Orientación vs tiempo')
axs2.legend()

# %%

# %% Creamos la figura
fig = plt.figure(figsize=(8,8))
axs=plt.subplot(111)

axs.plot(xc[0:total],yc[0:total], color="blue", label="Circular motion")
axs.scatter(xd[-1], yd[-1], color='Green', linewidth=10, marker='o')
axs.scatter(0, 0, color='Red', linewidth=10, marker='o')
axs.set(xlabel=' Posición en x (m)', ylabel = 'Posición en y (m)')
axs.set_title('Posición en Y vs Posición en X')
axs.text(2.6, 1.9, "Punto\ndeseado", color='Black')# Mostramos el gráfico
axs.text(0, 0.05, "Punto\ninicio", color='Black')# Mostramos el gráfico
plt.show()

# %%
# Creamos la figura
fig = plt.figure(figsize=(14,10))
# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensionaligsize()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')

# Datos en array bi-dimensional
z = np.zeros((1,len(xc)))
ax1.plot_wireframe(xc, yc, z, color= "blue")
ax1.set(xlabel="Posición en X (m)", ylabel="Posición en Y (m)", zlabel="Posición en Z (m)")
ax1.scatter(xd[-1], yd[-1], z[-1], color='Green', linewidth=12, marker='o')
ax1.scatter(0, 0, 0, color='Red', linewidth=12, marker='o')
#ax1.text(xd[-1], yd[-1],z[-1]+0.2, 'Mínimo', fontsize = 10, horizontalalignment='center', verticalalignment='center')  # Colocamos texto cerca del valor donde se encuentra el mínimo
ax1.text(3, 1.82, 0.014, "Punto\ndeseado", color='Black')# Mostramos el gráfico
ax1.text(0, 0, 0.014, "Punto\ninicio", color='Black')# Mostramos el gráfico

plt.show()