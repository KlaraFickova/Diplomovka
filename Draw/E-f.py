import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi

inputName = "21cylindrov"
fileName = inputName + "-E-f"
plotName = fileName + "-smery"
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

print(E.shape)

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

colors = mpl.colors.hsv_to_rgb([np.array([h,1,1]) for h in np.linspace(0,1,RkCount,endpoint=False)][::-1])

plt.figure ( figsize = (10,3) )
for ir in range(RkCount):
    plt.plot(frequencies, np.abs(E[:,ir]), color=colors[ir], label = "%5.1f" %(Rk[ir]) )
#plt.ylim(bottom=1e-6)
plt.legend(loc=1)
#plt.yscale("log")

plt.savefig("./"+plotName+".pdf")
#plt.show ()
