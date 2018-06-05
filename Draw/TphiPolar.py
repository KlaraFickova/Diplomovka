import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "1dipol1"
fileName = inputName + "-Tphi2"
plotName = fileName + "-polar"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
Tphi    = data['Tphi']
frequencies= data['frequencies']
Rk      = data['Rk']

print(Tphi.shape)
ax = plt.subplot(111, projection='polar')
idx=419
for i in [idx]:
    ax.plot(phi, Tphi[idx,:])
#ax.set_rmin(-20)
#ax.set_rscale('log')
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
#ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
#ax.grid(True)

#plt.figure ( figsize = (10, 10) )
#imgplot = plt.polar ( phi, Tphi )

ax.set_title (r'$f = $'+str(float(frequencies[idx])) + r', $R_k = $'+str(float(Rk)), va='bottom')
plt.savefig("./"+plotName+".pdf")
#plt.show ()
