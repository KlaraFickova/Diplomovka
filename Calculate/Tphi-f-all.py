import numpy as np
import matplotlib as mpl
from scipy import special as bessel # we will use only bessel functions
from numpy import pi

inputName   = "1dipol4"
outputName  = inputName + "-" + "Tphi-all"

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

Rk=1000
phiCount = 361
phi = np.linspace(0, 2*pi, phiCount)
phi = phi.reshape((1,-1,1))

mi0     = 1.         # arbitrary units

omega   = 2*pi * frequencies.reshape(-1,1)
lambd = 1./frequencies.reshape((-1,1))
lambd[0,0]=0
kv 		= omega.reshape(-1,1,1)         # /c, c=1

m=m.reshape(1,1,-1)
Ezout   = np.zeros((countf, phiCount), dtype= np.complex128)
Hphiout = np.zeros((countf, phiCount), dtype=np.complex128)
#(countf, phicount, m)
for i in range(n):
    point = Rk*np.exp(1j*phi)-(x0[i]+1j*y0[i]) # we use complex number as a representation of coordinates in 2D plane
    ri, phii = np.abs(point), np.angle(point)
    Ezout += np.sum(
        beta[:, i, :].reshape((countf,1,-1)) * bessel.hankel1(m, kv * ri) * np.exp(1j*m*phii),
        axis = 2)
    Hphiout += lambd/(1j*mi0) * np.sum(
        kv * beta[:, i, :].reshape((countf,1,-1)) * bessel.h1vp(m, kv * ri) * np.exp(1j*m*phii) * np.cos(phi-phii) +
        1/ri * 1j*m * beta[:, i, :].reshape((countf,1,-1)) * bessel.hankel1(m, kv * ri) * np.exp(1j*m*phii) * np.sin(phi-phii),
        axis = 2)
Tphi=1./2*np.real( Ezout * np.conj(Hphiout) )

phi = phi.reshape((-1))
np.savez ("./Results/" +outputName+ ".npz", frequencies=frequencies, Rk=Rk, phi=phi, Tphi=Tphi)
