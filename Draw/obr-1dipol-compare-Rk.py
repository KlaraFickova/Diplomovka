import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "1dipol1"
fileName1 = inputName + "-Tphi1a"
fileName2 = inputName + "-Tphi1b"
fileName3 = inputName + "-Tphi1c"
plotName = "1dipol-compare-Rk"
inputData = np.load("./Inputs/" + inputName + ".npz")
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
data3 = np.load("./Results/"+fileName3+".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data1['phi']
Tphi1   = data1['Tphi']
Tphi2   = data2['Tphi']
Tphi3   = data3['Tphi']
f       = data1['f']
Rk1      = data1['Rk']
Rk2      = data2['Rk']
Rk3      = data3['Rk']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

print(phi.shape, Tphi1.shape, Tphi2.shape, Tphi3.shape)

plt.figure ( figsize = (6,6) )
ax = plt.subplot(111, projection='polar')
ax.plot(phi, Rk1 * Tphi1, label=r'$R_k = $'+str(int(Rk1)))
ax.plot(phi, Rk2 * Tphi2, label=r'$R_k = $'+str(int(Rk2)))
ax.plot(phi, Rk3 * Tphi3, label=r'$R_k = $'+str(int(Rk3)))
ax.legend()

ax.set_title (r'$f = $'+str(float(f))+ r", $R=0.45$, $\epsilon=(3.5 \pm 0.05 \mathrm{i})^2$", y=1.08)
plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
