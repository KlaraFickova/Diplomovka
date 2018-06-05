import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "1cylinder2"
fileName1 = inputName + "-E-y-1"
fileName2 = inputName + "-E-y-2"
plotName = "1cyl-E-y-min-vs-max"
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n       = inputData['n']
R       = inputData['R']
epsilon = inputData['epsilon']
x0      = inputData['x']
y0      = inputData['y']

E1       = data1['E']
f1       = data1['f']
E2       = data2['E']
f2       = data2['f']
X       = data1["X"]
Y       = data1["Y"]

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7, 3) )
plt.plot(Y, np.abs(E1[:,0]), label='$f=0.152$')
plt.plot(Y, np.abs(E2[:,0]), label='$f=0.166$')
plt.legend()
plt.ylim(top=2, bottom=0)
plt.xlabel(r"$y$")
plt.ylabel(r"$|E|$")
plt.title( r"$x=0$" )

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
