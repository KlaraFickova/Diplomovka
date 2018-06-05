# We have n dielectric cylinders
import numpy as np
import scipy.special as bessel    #we will only use bessel functions
from numpy import pi
import os

inputName = "1dipol1test"

inputData 		= np.load("./Inputs/"+inputName+".npz")

countf		= inputData['countf']
frequencies = inputData['frequencies']

n 		= inputData['n']
mrow 	= inputData['mrow']
m 		= inputData['m']
mmax 	= inputData['mmax']

epsilon = inputData['epsilon']
mi		= inputData['mi']
zeta    = inputData['zeta']

x		= inputData['x']
y		= inputData['y']
R		= inputData['R']
gama	= inputData['gama']
a		= inputData['a']

# Creating numpy arrays
A = np.zeros ((2*m.size*n, 2*m.size*n), dtype=np.complex128)
v = np.zeros ((2*m.size*n, 1), dtype=np.complex128)
alpha = np.zeros ((countf, n, m.size), dtype=np.complex128)
beta  = np.zeros ((countf, n, m.size), dtype=np.complex128)

for idx, f in enumerate(frequencies):
	# Frequency dependant variables
	kv = 2*pi * f               #wavenumber in vacuum
	k = np.sqrt(epsilon*mi)*kv  #wavenumber in cylinders
	#lam = 1./ f                #wavelength

	for i in range(n):
		for j in range(n):
			if i==j:
				A[m.size*(2*i  ) : m.size*(2*i+1), m.size* 2*j    : m.size*(2*j+1)]  =  np.diag (            bessel.jv      (mrow, k[i]*R[i]) )
				A[m.size*(2*i  ) : m.size*(2*i+1), m.size*(2*j+1) : m.size*(2*j+2)]  =  np.diag (          - bessel.hankel1 (mrow, kv  *R[i]) )
				A[m.size*(2*i+1) : m.size*(2*i+2), m.size* 2*j    : m.size*(2*j+1)]  =  np.diag ( 1/zeta[i]* bessel.jvp     (mrow, k[i]*R[i]) )
				A[m.size*(2*i+1) : m.size*(2*i+2), m.size*(2*j+1) : m.size*(2*j+2)]  =  np.diag (          - bessel.h1vp    (mrow, kv  *R[i]) )
			else:
				A[m.size*(2*i  ) : m.size*(2*i+1), m.size* 2*j    : m.size*(2*j+1)]  =  0
				A[m.size*(2*i  ) : m.size*(2*i+1), m.size*(2*j+1) : m.size*(2*j+2)]  =  -bessel.hankel1(mrow-m, kv*a[i,j]) * bessel.jv (m, kv*R[i])* np.exp(1j*(mrow-m)*gama[j,i])
				A[m.size*(2*i+1) : m.size*(2*i+2), m.size* 2*j    : m.size*(2*j+1)]  =  0
				A[m.size*(2*i+1) : m.size*(2*i+2), m.size*(2*j+1) : m.size*(2*j+2)]  =  -bessel.hankel1(mrow-m, kv*a[i,j]) * bessel.jvp(m, kv*R[i])* np.exp(1j*(mrow-m)*gama[j,i])

	for i in range(n):
		v[(2*i  )*m.size : (2*i+1)*m.size]  =  bessel.jv ( m, kv*R[i] ) * np.exp( 1j*kv* y[i] )
		v[(2*i+1)*m.size : (2*i+2)*m.size]  =  bessel.jvp( m, kv*R[i] ) * np.exp( 1j*kv* y[i] )


	try:
		alphabeta = np.linalg.solve(A,v).reshape(n, 2, m.size)
		alpha [idx,:,:] = alphabeta [:,0,:]
		beta  [idx,:,:] = alphabeta [:,1,:]
	except np.linalg.LinAlgError:
		pass


np.savez("./Results/"+ inputName +".npz", alpha=alpha, beta=beta )
