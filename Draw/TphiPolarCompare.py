import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName1 = "1dipol1"
inputName2 = "1dipol2"
fileName1 = inputName1 + "-Tphi1"
fileName2 = inputName2 + "-Tphi1"
plotName = "1dipol-polar-reverse"
data1 = np.load("./Results/"+fileName1+".npz")
inputData1 = np.load("./Inputs/" + inputName1 + ".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData2 = np.load("./Inputs/" + inputName2 + ".npz")

n   = inputData1['n']
R   = inputData1['R']
x0  = inputData1['x']
y0  = inputData1['y']

phi     = data1['phi']
Tphi1   = data1['Tphi']
Tphi2   = data2['Tphi']
f       = data1['f']
Rk      = data1['Rk']

ax = plt.subplot(111, projection='polar')
ax.plot(phi, Tphi1, 'b', -phi, Tphi2, 'r')
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
#ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

#plt.figure ( figsize = (10, 10) )
#imgplot = plt.polar ( phi, Tphi )

ax.set_title (r'$f = $'+str(float(f)) + r', $R_k = $'+str(float(Rk)), va='bottom')
plt.savefig("./"+plotName+".png")
#plt.show ()
