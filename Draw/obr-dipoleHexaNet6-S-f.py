import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "dipoleHexaNet6"
fileName = inputName + "-Tphi-all"
plotName = "dipoleHexaNet6-S-f"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n       = inputData['n']
R       = inputData['R']
epsilon = inputData['epsilon']
x0      = inputData['x']
y0      = inputData['y']

phi     = data['phi']
phiCount = phi.size
Tphi    = data['Tphi']
frequencies = data['frequencies']
countf = frequencies.size
Rk      = data['Rk']

S = 2*pi/phiCount * np.sum(Tphi, axis=1)
print(np.nanargmax(S)) # = 840
print(np.nanargmax(S[300:400])+300)
print(np.nanargmax(S[500:700])+500)

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7, 3) )
plt.plot(frequencies, S)
plt.ylim(top=100, bottom=1e-3)
plt.yscale("log")
plt.xlabel(r"$f$")
plt.ylabel(r"$S$")
plt.title( r"1 dipól, $R=0.45$, $\epsilon_{up} = (3.5 + 0.05\mathrm{i})^2$, $\epsilon_{down} = (3.5 - 0.05\mathrm{i})^2$" )

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
