import numpy as np
from scipy import special as bessel # we will use only bessel functions
from numpy import pi

inputName   = "1dipol1"
outputName  = inputName + "-" + "Tphi1c"

resultsData     = np.load("./Results/"+inputName+".npz")
inputData 		= np.load("./Inputs/"+inputName+".npz")

frequencies = inputData['frequencies']
alpha 		= resultsData['alpha']				#alpha[f,n,m]
beta 		= resultsData['beta']				#beta[f,n,m]

n 		= inputData['n']
mrow 	= inputData['mrow']
m 		= mrow.reshape(1,-1)
mmax 	= alpha.shape[2] // 2

epsilon = inputData['epsilon']
mi		= inputData['mi']
mi0     = 1.         # arbitrary units
idx		= np.argmin(np.abs(frequencies-0.838))
f		= frequencies[idx]
omega   = 2*pi * f
kv 		= omega         # /c, c=1

x0		= inputData['x']
y0		= inputData['y']
R		= inputData['R']
gama	= inputData['gama']
a		= inputData['a']

Rk=1000
phiCount = 361
phi = np.linspace(0, 2*pi, phiCount)

phi = phi.reshape(-1,1)
Ezout = np.zeros((phiCount), dtype= np.complex128)
Hphiout = np.zeros((phiCount), dtype=np.complex128)
for i in range(n):
    point = Rk*np.exp(1j*phi)-(x0[i]+1j*y0[i]) # we use complex number as a representation of coordinates in 2D plane
    ri, phii = np.abs(point), np.angle(point)
    Ezout += np.sum(
        beta[idx, i, :].reshape((1,-1)) * bessel.hankel1(m, kv * ri) * np.exp(1j*m*phii),
        axis = 1)
    Hphiout += 1/(1j*omega*mi0) * np.sum(
        kv * beta[idx, i, :].reshape((1,-1)) * bessel.h1vp(m, kv * ri) * np.exp(1j*m*phii) * np.cos(phi-phii) +
        1/ri * 1j*m * beta[idx, i, :].reshape((1,-1)) * bessel.hankel1(m, kv * ri) * np.exp(1j*m*phii) * np.sin(phi-phii),
        axis = 1)
phi = phi.reshape((-1))
Tphi=1./2*np.real( Ezout * np.conj(Hphiout) )

np.savez ("./Results/" +outputName+ ".npz", f=f, idx=idx, Rk=Rk, phi=phi, Tphi=Tphi)
