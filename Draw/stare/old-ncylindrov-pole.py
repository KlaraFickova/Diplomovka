import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
from numpy import pi

data 		= np.load("./Results/ncylindrov2.npz")
frequencies = data['frequencies']
alpha 		= data['alpha']				#alpha[f,n,m]
beta 		= data['beta']				#beta[f,n,m]

n 		= alpha.shape[1]
mrow 	= data['mrow']
m 		= mrow.reshape(1,-1)
mmax 	= alpha.shape[2] // 2

epsilon = data['epsilon']
mi		= data['mi']
idx		= int( frequencies.size / 2.2 )
f		= frequencies[idx]
kv 		= 2*pi * f
k 		= np.sqrt( epsilon*mi )*kv

x0		= data['x']
y0		= data['y']
R		= data['R']
gama	= data['gama']
a		= data['a']

	
def polarR(x,y):
	return np.abs(x+1j*y)
def polarFi( x, y):
	return np.angle(x+1j*y)

Xleft 	= -2
Xright 	= 13
dX 		= 0.01
X 		= np.arange ( Xleft, Xright, dX )
Ydown 	= -1
Yup 	= 1
dY 		= dX
Y 		= np.arange ( Ydown, Yup, dY )

A = np.array( [ [ np.real( np.exp ( 1j* kv* y ) + \
	np.sum  ( beta[idx,:,:] * bessel.hankel1 ( m, kv*polarR( x-x0, y-y0 ).reshape(-1,1) ) * \
	np.exp  ( 1j*m* polarFi( x-x0, y-y0 ).reshape(-1,1) ) )) 	\
	         for x in X ] for y in Y ] )

for i in range(n):
	xleft 	= x0[i]-R[i]
	ixleft 	= int((xleft-Xleft)/dX)
	xright 	= x0[i]+R[i]
	ixright = int((xright-Xright)/dX)+1
	ydown 	= y0[i]-R[i]
	iydown 	= int((ydown-Ydown)/dY)
	yup 	= y0[i]+R[i]
	iyup 	= int((yup-Yup)/dY)+1
	
	for ix in range (ixleft, ixright) :
		for iy in range (iydown, iyup) :
			fi = polarFi( X[ix]-x0[i], Y[iy]-y0[i] )
			r = polarR( X[ix]-x0[i], Y[iy]-y0[i] )
			if r < R[i]:
				A [iy,ix] = np.real( np.sum( alpha[idx,i,:] * bessel.jv1 ( m, k[i]*r ) * \
				np.exp ( 1j*m* fi ) ) )


#bound = max( abs( a.max() ), abs( a.min() ) )
bound = 3
plt.figure ( figsize = (14, 5) )
imgplot=plt.imshow ( A, vmin = -bound, extent = [ Xleft, Xright, Ydown, Yup ], vmax = bound, origin = 'lower' , interpolation = 'gaussian' ) 
plt.xlabel (r'$x$')
plt.ylabel (r'$y$')
plt.title  (r'$f = $'+ str(f))
plt.colorbar ( imgplot, orientation='horizontal' )
plt.show ()

