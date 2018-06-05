import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "1dipol1"
fileName = inputName + "-Tphi2"
plotName = fileName + "-S"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
phiCount = phi.size
Tphi    = data['Tphi']
frequencies = data['frequencies']
countf = frequencies.size
Rk      = data['Rk']

S = 2*pi/phiCount * np.sum(Tphi, axis=1)
print(np.nanargmax(S)) # = 419

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.plot(frequencies, S)
plt.yscale("log")

plt.savefig("./"+plotName+".pdf")
#plt.show ()
