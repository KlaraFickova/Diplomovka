import numpy as np
import matplotlib as mpl
from scipy import special as bessel # we will use only bessel functions
from numpy import pi

inputName   = "21cylindrov"
outputName  = inputName + "-" + "E-f"

resultsData     = np.load("./Results/"+inputName+".npz")
inputData 		= np.load("./Inputs/"+inputName+".npz")

frequencies = inputData['frequencies']
countf      = inputData['countf']
alpha 		= resultsData['alpha']				#alpha[f,n,m]
beta 		= resultsData['beta']				#beta[f,n,m]

n 		= inputData['n']
mrow 	= inputData['mrow']
m 		= mrow.reshape(1,-1)
mmax 	= alpha.shape[2] // 2

epsilon = inputData['epsilon']
mi		= inputData['mi']

x0		= inputData['x']
y0		= inputData['y']
R		= inputData['R']
gama	= inputData['gama']
a		= inputData['a']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

Rk=np.array([10, 11, 12, 1000, 1001, 1002])
RkCount = Rk.size
phi = pi/2
Rk = Rk.reshape((1,-1,1))

mi0     = 1.         # arbitrary units

omega   = 2*pi * frequencies.reshape(-1,1)
lambd = 1./frequencies.reshape((-1,1))
lambd[0,0]=0
kv 		= omega.reshape(-1,1,1)         # /c, c=1

m=m.reshape(1,1,-1)
Ezout   = np.zeros((countf, RkCount), dtype= np.complex128)
#(countf, phicount, m)
for i in range(n):
    point = Rk*np.exp(1j*phi)-(x0[i]+1j*y0[i]) # we use complex number as a representation of coordinates in 2D plane
    ri, phii = np.abs(point), np.angle(point)
    Ezout += np.sum(
        beta[:, i, :].reshape((countf,1,-1)) * bessel.hankel1(m, kv * ri) * np.exp(1j*m*phii),
        axis = 2)

E = Ezout + np.exp( 1j*kv.reshape((-1,1))*Rk.reshape((1,-1)) )

Rk = Rk.reshape((-1))
np.savez ("./Results/" +outputName+ ".npz", frequencies=frequencies, Rk=Rk, phi=phi, E=E)
