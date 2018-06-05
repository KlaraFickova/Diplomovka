import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName1 = "1dipol1"
inputName2 = "1dipol2"
fileName1 = inputName1 + "-Tphi2"
fileName2 = inputName2 + "-Tphi2"
plotName = "1dipol-compare-Tup"
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

Tup1 = 2*pi/countf * Tphi1[:, 90]
Tup2 = 2*pi/countf * Tphi2[:, 90]
print(np.nanargmax(Tup1)) # = 419
print(np.nanargmax(Tup2)) # = 419

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7,3) )
plt.plot(frequencies, Tup1*1.1)
plt.plot(frequencies, Tup2)
plt.ylim(top=1e-1, bottom=1e-7)
plt.yscale("log")

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
