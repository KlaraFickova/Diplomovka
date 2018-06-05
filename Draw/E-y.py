import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "1cylinder2"
fileName = inputName + "-E-y-2"
plotName = fileName
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n       = inputData['n']
R       = inputData['R']
epsilon = inputData['epsilon']
x0      = inputData['x']
y0      = inputData['y']

E       = data['E']
f       = data['f']
X       = data["X"]
Y       = data["Y"]
idx     = data["idx"]

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

plt.figure ( figsize = (7, 3) )
plt.plot(Y, np.abs(E[:,0]))
plt.ylim(top=2, bottom=0)
plt.xlabel(r"$y$")
plt.ylabel(r"$E$")
plt.title( r"$R=0.45$" )

plt.tight_layout()
plt.savefig("./"+plotName+".pdf", bbox_inches='tight')
#plt.show ()
