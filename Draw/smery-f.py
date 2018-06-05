import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "21cylindrov"
fileName = inputName + "-Tphi-all"
plotName = fileName + "-smery"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
Tphi    = data['Tphi']
frequencies = data['frequencies']
countf = frequencies.size
Rk      = data['Rk']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

for uhol in range(90,360,180):
    plt.plot(frequencies, 2*pi/countf * Tphi[:,uhol]*(1+uhol/1000.), label = "%d" %(uhol) )
#plt.ylim(bottom=1e-6)
plt.legend(loc=4)
#plt.yscale("log")

plt.savefig("./"+plotName+".pdf")
#plt.show ()
