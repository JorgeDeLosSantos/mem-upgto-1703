# -*- coding: utf-8 -*-
import numpy as np
from numpy import pi,cos,sin,tan,exp,log,arcsin,arccos,arctan
import matplotlib.pyplot as plt

def plotvector(p0,u,color="r"):
    """
    Gráfica un vector, dados su punto inicial 
    y sus componentes rectangulares
    """
    plt.plot([p0[0],p0[0]+u[0]],[p0[1],p0[1]+u[1]],color)
    
    
if __name__ == '__main__':
    plotvector([0,0],[10,1])

