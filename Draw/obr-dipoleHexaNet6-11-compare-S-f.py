import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName1 = "dipoleHexaNet6"
inputName2 = "dipoleHexaNet11"
fileName1 = inputName1 + "-Tphi-all"
fileName2 = inputName2 + "-Tphi-all"
plotName = "dipoleHexaNet6-11-compare-S-f"
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData = np.load("./Inputs/" + inputName1 + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data1['phi']
Tphi1    = data1['Tphi']
Tphi2    = data2['Tphi']
frequencies = data1['frequencies']
countf = frequencies.size
Rk      = data1['Rk']

S1 = 2*pi/countf * np.sum(Tphi1, axis=1)
S2 = 2*pi/countf * np.sum(Tphi2, axis=1)
print(np.nanargmax(S1)) # = 419
print(np.nanargmax(S2)) # =

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7,3) )
plt.plot(frequencies, S1)
plt.plot(frequencies, S2)
#plt.ylim(top=10, bottom=1e-3)
plt.yscale("log")
plt.xlabel(r"$f$")
plt.ylabel(r"$S$")
plt.title( r"$R=0.45$, $\epsilon = (1.1 \pm 0.1\mathrm{i})^2$" )

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
