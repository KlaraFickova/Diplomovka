import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName1 = "1dipol1"
inputName2 = "1dipol2"
fileName1 = inputName1 + "-Tphi1"
fileName2 = inputName2 + "-Tphi1"
plotName = "1dipol-compare-polar"
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

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (6,6) )
ax = plt.subplot(111, projection='polar')
ax.plot(phi, Tphi1, 'c', label=r"$\pm$")
ax.plot(phi, Tphi2, 'm', label=r"$\mp$")
ax.legend()
plt.title (r'$f = $'+str(float(f)) + r', $R_k = $'+str(Rk)+r", $R=0.45$, $\epsilon = (3.5 \pm(\mp) 0.05\mathrm{i})^2$", y=1.08)

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
