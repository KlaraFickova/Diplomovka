import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "dipoleHexaNet11"
fileName = inputName + "-Tphi-all"
plotName = inputName+"-max-polar"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
Tphi   = data['Tphi']
frequencies = data['frequencies']
Rk      = data['Rk']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

idx = 350
f = frequencies[idx]

plt.figure ( figsize = (6,6) )
ax = plt.subplot(111, projection='polar')
#Tphi=np.where(Tphi<0 || !Tphi, 0, Tphi)
ax.plot(phi, Tphi[idx,:])
ax.set_rlabel_position(35)

ax.set_title (r'$f = $ %4.3f, $R_k = $ %d, $R=0.45$, $\epsilon=1.1\pm  0.1 \mathrm{i}$'%(f, Rk), y=1.08)
plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
