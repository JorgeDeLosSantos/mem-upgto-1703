# -*- coding: utf-8 -*-
import numpy as np
from numpy import pi,cos,sin,tan
import matplotlib.pyplot as plt

r2, r3 = 3, 8
t2 = np.linspace(0,2*pi,6)
t3 = np.arcsin(-r2*sin(t2)/r3)
r1 = r2*cos(t2) + r3*cos(t3)
colores = ["r","b","g","y","m","k"]

for k in range(len(t2)):
    plt.plot([0,r2*cos(t2[k])],[0,r2*sin(t2[k])],colores[k])
    plt.plot([r2*cos(t2[k]),r2*cos(t2[k])+r3*cos(t3[k])],[r2*sin(t2[k]),r2*sin(t2[k])+r3*sin(t3[k])],colores[k])

plt.show()




