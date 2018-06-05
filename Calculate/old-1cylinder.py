import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

# Precision integers
mmax = 10
mrow = np.arange(-mmax,mmax+1)
countf = 10000

# Environment variables and constants
frequencies = np.linspace (0, 2, countf)
epsilon = 60.
mi = 1.
zeta = np.sqrt (mi/epsilon)

# Geometry
R = 0.4
x = 0
y = 0

alpha = np.empty ( (mmax, countf), dtype = np.complex128 )
beta = np.empty ( (mmax, countf), dtype = np.complex128 )

for idx in range (countf):
	f = frequencies [idx]
	kv = 2*np.pi *f
	k = math.sqrt ( epsilon* mi ) * kv

	for m in range (mmax):
		A = np.array( [ [ bessel.jv (m, k*R), -bessel.hankel1 (m, kv*R) / bessel.h1vp (m, kv*R) ],\
					  [ 1./zeta *bessel.jvp (m, k*R), -1 ]])
		y = np.array( [ [ bessel.jv (m, kv*R)], [bessel.jvp (m, kv*R) ] ] )

		if ( np.linalg.det(A) != 0 ):
			x = np.linalg.solve ( A, y )
		else:
			x = np.array ([[0],[0]])
		alpha [m, idx] = x[0,0]
		beta [m, idx] = x[1,0]

np.savez ( "./Results/1cylinder1.npz", frequencies=frequencies, alpha=alpha, beta=beta, R=R, epsilon=epsilon, mi=mi, zeta=zeta, mrow=mrow )
