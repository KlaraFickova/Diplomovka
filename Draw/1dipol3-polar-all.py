#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "1dipol3"
fileName = inputName + "-Tphi-all"
plotName = inputName + "-polar-all"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n   = inputData['n']
R   = inputData['R']
x0  = inputData['x']
y0  = inputData['y']

phi     = data['phi']
Tphi    = data['Tphi']
frequencies= data['frequencies']
countf      =frequencies.size
Rk      = data['Rk']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'


plt.figure ( figsize = (6,6) )
ax = plt.subplot(111, projection='polar')
plt.title(r"1 dipól", y=1.08)
colors = mpl.colors.hsv_to_rgb([np.array([h,1,1]) for h in np.linspace(0,1,countf,endpoint=False)])
#Tphi = np.where(Tphi<0, 0, Tphi)
for idx in range(1,countf):
    ax.plot (  phi, Tphi[idx,:]/np.max(Tphi[idx,:]), '-', color=colors[idx] )

plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
