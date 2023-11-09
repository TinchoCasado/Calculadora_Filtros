# -*- coding: utf-8 -*-

'''
Iván Rodríguez - 2017
Código generado para el canal de YouTube Piensa 3D
'''

# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

# Código de cálculos y entrada
r = float(input("Ingrese el valor de resistencia (en ohms): \n"))
c = float(input("Ingrese el valor de capacitor (en microfaradios): \n"))
c = float(c*0.000001)

# Generamos los datos para el gráfico
x = np.array(range(5000))*1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = (1/(2*math.pi*(x[i])*r*c+1))

# Creamos el gráfico
plt.ion()
plt.xscale("log")
plt.plot(x,y)
