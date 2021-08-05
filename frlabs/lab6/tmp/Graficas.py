#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:47:35 2021

@author: diegopalma
"""

import numpy as np
import matplotlib.pyplot as plt

print("Loading data from files...")

xcurrent = open("xactual_op2.txt", 'r')
xdesired = open("xdeseado_op2.txt", 'r') 
qcurrent = open("qactual_op2.txt",'r')
qdesired = open("qdeseado_op2.txt",'r')

timec=np.array([])
timed=np.array([])
# ---- X actual ---
xc_x=np.array([]); xc_y=np.array([]); xc_z=np.array([])
# ---- X deseado ---
xd_x=np.array([]); xd_y=np.array([]); xd_z=np.array([])
# ---- q actual ---
qc0=np.array([]); qc1=np.array([]); qc2=np.array([])
qc3=np.array([]); qc4=np.array([]); qc5=np.array([])
qc6=np.array([])
# ---- q deseado ---
qd0=np.array([]); qd1=np.array([]); qd2=np.array([])
qd3=np.array([]); qd4=np.array([]); qd5=np.array([])
qd6=np.array([])

freq = 20
dt = 1.0/freq

# Leer Datos de los valores actuales
for line in xcurrent:
    line = xcurrent.readline()
    xyz=line.split()
    try:
        t=float(xyz[0]); timec=np.append(timec, t)
        x=float(xyz[1]); xc_x=np.append(xc_x, x)
        y=float(xyz[2]); xc_y=np.append(xc_y, y)
        z=float(xyz[3]); xc_z=np.append(xc_z, z)
    except:
        pass

# Leer Datos de los valores deseados
for line in xdesired:
    line = xdesired.readline()
    xyz=line.split()
    try:
        t=float(xyz[0]); timed=np.append(timed, t)
        x=float(xyz[1]); xd_x=np.append(xd_x, x)
        y=float(xyz[2]); xd_y=np.append(xd_y, y)
        z=float(xyz[3]); xd_z=np.append(xd_z, z)
    except:
        pass

for line in qcurrent:
    line = qcurrent.readline()
    xyz=line.split()
    try:
        q_0=float(xyz[0]); qc0=np.append(qc0, q_0)
        q_1=float(xyz[1]); qc1=np.append(qc1, q_1)
        q_2=float(xyz[2]); qc2=np.append(qc2, q_2)
        q_3=float(xyz[3]); qc3=np.append(qc3, q_3)
        q_4=float(xyz[4]); qc4=np.append(qc4, q_4)
        q_5=float(xyz[5]); qc5=np.append(qc5, q_5)
        q_6=float(xyz[6]); qc6=np.append(qc6, q_6)
    except:
        pass
for line in qdesired:
    line = qdesired.readline()
    xyz=line.split()
    try:
        q_0=float(xyz[0]); qd0=np.append(qd0, q_0)
        q_1=float(xyz[1]); qd1=np.append(qd1, q_1)
        q_2=float(xyz[2]); qd2=np.append(qd2, q_2)
        q_3=float(xyz[3]); qd3=np.append(qd3, q_3)
        q_4=float(xyz[4]); qd4=np.append(qd4, q_4)
        q_5=float(xyz[5]); qd5=np.append(qd5, q_5)
        q_6=float(xyz[6]); qd6=np.append(qd6, q_6)
    except:
        pass

    
# %% 
total=len(qc0)
tiempo=dt*np.arange(0,total)

#fig, axs = plt.subplots(2,2)

fig= plt.figure(figsize=(20,10))

fig.suptitle("Configuración articular", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(231)
axs1=plt.subplot(232)
axs2=plt.subplot(233)
axs3=plt.subplot(234)
axs4=plt.subplot(235)
axs5=plt.subplot(236)

axs0.plot(qc0[0:total], qc1[0:total], color="blue", label= "Configuración articular 0")
axs0.plot(qc0[0:total], qd1[0:total], color="green", label= "Configuración deseada 0")
axs0.set(xlabel='Tiempo (s)', ylabel='Configuración articular 0 (rad)')
axs0.set_title('q0 vs tiempo')
axs0.legend()

axs1.plot(qc0[0:total], qc2[0:total], color="blue", label= "Configuración articular 1")
axs1.plot(qc0[0:total], qd2[0:total], color="green", label= "Configuración deseada 1")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Configuración articular 1 (rad)')
axs1.set_title('q1 vs tiempo')
axs1.legend()

axs2.plot(qc0[0:total], qc3[0:total], color="blue", label= "Configuración articular 2")
axs2.plot(qc0[0:total], qd3[0:total], color="green", label= "Configuración deseada 2")
axs2.set(xlabel='Tiempo (s)', ylabel='Configuración articular 2 (rad)')
axs2.set_title('q2 vs tiempo')
axs2.legend()

axs3.plot(qc0[0:total], qc4[0:total], color="blue", label= "Configuración articular 3")
axs3.plot(qc0[0:total], qd4[0:total], color="green", label= "Configuración deseada 3")
axs3.set(xlabel='Tiempo (s)', ylabel='Configuración articular 3 (rad)')
axs3.set_title('q3 vs tiempo')
axs3.legend()

axs4.plot(qc0[0:total], qc5[0:total], color="blue", label= "Configuración articular 4")
axs4.plot(qc0[0:total], qd5[0:total], color="green", label= "Configuración deseada 4")
axs4.set(xlabel= 'Tiempo (s)', ylabel='Configuración articular 4 (rad)')
axs4.set_title('q4 vs tiempo')
axs4.legend()

axs5.plot(qc0[0:total], qc6[0:total], color="blue", label= "Configuración articular 5")
axs5.plot(qc0[0:total], qd6[0:total], color="green", label= "Configuración deseada 5")
axs5.set(xlabel='Tiempo (s)', ylabel='Configuración articular 5 (rad)')
axs5.set_title('q5 vs tiempo')
axs5.legend()

# %% 
total=len(xc_x)
tiempo=dt*np.arange(0,total)

#fig, axs = plt.subplots(2,2)

fig= plt.figure(figsize=(12,9))

fig.suptitle("Posiciones cartesianas", fontsize=20,x=0.5,y=0.94)
axs0=plt.subplot(221)
axs1=plt.subplot(222)
axs2=plt.subplot(212)

axs0.plot(timec, xc_x[0:total], color="blue", label= "Posición actual de x")
axs0.plot(timed, xd_x[0:total], color="green", label= "Posición deseada de x")
axs0.set(xlabel='Tiempo (s)', ylabel='Posición en x (m)')
axs0.set_title('Posición en X vs tiempo')
axs0.legend()

axs1.plot(timec, xc_y[0:total], color="blue", label= "Posición actual de y")
axs1.plot(timed, xd_y[0:total], color="green", label= "Posición deseada de y")
axs1.set(xlabel= 'Tiempo (s)', ylabel='Posición en y (m)')
axs1.set_title('Posición en Y vs tiempo')
axs1.legend()

axs2.plot(timec, xc_z[0:total], color="blue", label= "Posición actual de z")
axs2.plot(timed, xd_z[0:total], color="green", label= "Posición deseada de z")
axs2.set(xlabel='Tiempo (s)', ylabel='Posición en y (m)')
axs2.set_title('Posición en Z vs tiempo')
axs2.legend()