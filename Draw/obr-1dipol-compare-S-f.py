import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName1 = "1dipol1"
inputName2 = "1dipol2"
fileName1 = inputName1 + "-Tphi2"
fileName2 = inputName2 + "-Tphi2"
plotName = "1dipol-compare-S-f"
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData = np.load("./Inputs/" + inputName1 + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data1['phi']
phiCount = phi.size
Tphi1    = data1['Tphi']
Tphi2    = data2['Tphi']
frequencies = data1['frequencies']
countf = frequencies.size
Rk      = data1['Rk']

S1 = 2*pi/phiCount * np.sum(Tphi1, axis=1)
S2 = 2*pi/phiCount * np.sum(Tphi2, axis=1)
print(np.nanargmax(S1)) # = 419
print(np.nanargmax(S2)) # =

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7,3) )
plt.plot(frequencies, S1, 'c', label=r"$\pm$")
plt.plot(frequencies, S2, 'm', label=r"$\mp$")
plt.ylim(top=10, bottom=1e-3)
plt.yscale("log")
plt.xlabel(r"$f$")
plt.ylabel(r"$S$")
plt.legend()
plt.title( r"$R=0.45$, $\epsilon = (3.5 \pm (\mp) 0.05\mathrm{i})^2$" )

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
