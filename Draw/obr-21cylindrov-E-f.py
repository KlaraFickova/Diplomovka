import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "21cylindrov"
fileName = inputName + "-E-f"
plotName = fileName
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
E    = data['E']
frequencies = data['frequencies']
countf = frequencies.size
Rk      = data['Rk']
RkCount = Rk.size

print(np.argmin(np.abs(E[400:,4]))+400)
print(np.argmax(np.abs(E[400:,4]))+400)

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

colors = mpl.colors.hsv_to_rgb([np.array([h,1,1]) for h in np.linspace(0,1,RkCount,endpoint=False)][::-1])

plt.figure ( figsize = (10,4) )
plt.subplot(2,1,1)
for ir in range(0,3):
    plt.plot(frequencies, np.abs(E[:,ir]), color=colors[ir], label = r"$Y=\,$%d" %(Rk[ir]) )
#plt.ylim(bottom=1e-6)
plt.legend(loc=1)
plt.ylabel(r'$|E\,[0,Y]|$')
#plt.yscale("log")
plt.subplot(2,1,2)
for ir in range(3,6):
    plt.plot(frequencies, np.abs(E[:,ir]), color=colors[ir], label = r"$Y=\,$%d" %(Rk[ir]) )
#plt.ylim(bottom=1e-6)
plt.legend(loc=1)
plt.xlabel('f')
plt.ylabel(r'$|E\,[0,Y]|$')
#plt.yscale("log")

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches="tight")
#plt.show ()
