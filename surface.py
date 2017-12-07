#!/usr/bin/env python
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = [1,1,1,1,2,2,2,2,3,3,3,3]
Y = [1,4,5,6,1,4,5,6,1,4,5,6]
Z = [2,6,3,6,2,7,4,6,2,4,2,3]

plotx,ploty, = np.meshgrid(np.linspace(np.min(X),np.max(X),10),\
                           np.linspace(np.min(Y),np.max(Y),10))
plotz = interp.griddata((X,Y),Z,(plotx,ploty),method='linear')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(plotx,ploty,plotz,cstride=1,rstride=1,cmap='viridis')  # or 'hot'
