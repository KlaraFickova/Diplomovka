import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.colors import hsv_to_rgb
import time

start = time.time()
print (start)

resultsData 		= np.load("./Results/1dipol1.npz")
inputData 		= np.load("./Inputs/1dipol1.npz")
frequencies = inputData['frequencies']
alpha 		= resultsData['alpha']				#alpha[f,n,m]
beta 		= resultsData['beta']				#beta[f,n,m]

n 		= alpha.shape[1]
mrow 	= inputData['mrow']
m 		= mrow.reshape(1,-1)
mmax 	= alpha.shape[2] // 2

epsilon = inputData['epsilon']
mi		= inputData['mi']
idx		= int( 420 )
f		= frequencies[idx]
kv 		= 2*pi * f
k 		= np.sqrt( epsilon*mi )*kv

x0		= inputData['x']
y0		= inputData['y']
R		= inputData['R']
gama	= inputData['gama']
a		= inputData['a']

print (time.time() - start, "arrays loaded")

def Complex2HSV(z, rmin, rmax, hue_start=90):
    # get amplidude of z and limit to [rmin, rmax]
    amp = np.abs(z)
    amp = np.where(amp < rmin, rmin, amp)
    amp = np.where(amp > rmax, rmax, amp)
    ph = np.angle(z, deg=1) + hue_start
    # HSV are values in range [0,1]
    #h = 0.5 + 0.2 * np.sin((ph % 360) / 360 *2*pi)	#blue-green
    h = 0.6 + 0.1 * np.sin((ph % 360.) / 360. *2.*pi)
    #h = (ph % 360) / 360				#cheesy rainbow
    s = (amp -rmin) / (rmax - rmin)
    v = 1*np.ones_like(h)
    #s = 0.85 *
    #v = (amp -rmin) / (rmax - rmin)
    return hsv_to_rgb(np.dstack((h,s,v)))

def Complex2RGB (z, rmin, rmax) :
    # set middle color
    hue_start = 170.
    # get amplidude of z and limit to [rmin, rmax]
    amp = np.abs(z)
    h = hue_start + 10 * (np.real(z) / amp) 		#hue = 160° +- 10°
    s = (amp -rmin) / (rmax - rmin)
    s = np.where (s < 0, 0., s)
    s = np.where (s > 1, 1., s)
    v = 1.*np.ones_like(h)

    c = v * s
    x = c * (1 - abs((h / 60.) % 2. - 1.))
    m = v - c

    r,g,b = 0.,c,x
    r,g,b = (r+m), (g+m), (b+m)

    return np.dstack((r,g,b))

def polarR(x,y):
	return np.abs(x+1j*y)
def polarFi( x, y):
	return np.angle(x+1j*y)


print (time.time() - start, "functions defined")

Xleft 	= -3
Xright 	= 3
dX 		= 0.02
X 		= np.arange ( Xleft, Xright, dX )
Ydown 	= -3
Yup 	= 3
dY 		= dX
Y 		= np.arange ( Ydown, Yup, dY )
"""
A = np.array( [ [ np.exp ( 1j* kv* y ) + \
	np.sum  ( beta[idx,:,:] * bessel.hankel1 ( m, kv*polarR( x-x0, y-y0 ).reshape(-1,1) ) * \
	np.exp  ( 1j*m* polarFi( x-x0, y-y0 ).reshape(-1,1) ) ) 	\
	        for x in X ] for y in Y ] )
"""
#A1, A2, A3 = [np.empty ( (Y.size, X.size, n, m.size), dtype=np.complex128 )]*3
#print(A1.shape)
A1 = np.exp  ( 1j* kv* Y.reshape(-1,1) )
A2 = beta[idx,:,:].reshape( 1,1,n,-1 ) * bessel.hankel1 ( m.reshape(1,1,1,-1), kv*polarR( X.reshape(1,-1,1,1)-x0.reshape(1,1,n,1), Y.reshape(-1,1,1,1)-y0.reshape(1,1,n,1) ) )
A3 = np.exp  ( 1j*m.reshape(1,1,1,-1) * polarFi( X.reshape(1,-1,1,1)-x0.reshape(1,1,n,1), Y.reshape(-1,1,1,1)-y0.reshape(1,1,n,1) ) )
A  = A1 +  np.sum ( (A2*A3), axis =(2,3) )
print (A1.shape, A2.shape, A3.shape, A.shape)

print (time.time() - start, "basic A computed")

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
				A [iy,ix] = np.sum( alpha[idx,i,:] * bessel.jv1 ( m, k[i]*r ) * \
				np.exp ( 1j*m* fi ) )


print (time.time() - start, "A inside cylinders computed")

np.savez ("./pole.npz", A=A)
#bound = max( abs( a.max() ), abs( a.min() ) )
bound = 3
plt.figure ( figsize = (14, 5) )
ColorA = Complex2RGB(A, 0., 2.)
imgplot = plt.imshow ( ColorA,  extent = [ Xleft, Xright, Ydown, Yup ], origin = 'lower' , interpolation = 'gaussian' )

ax=plt.gca()
circle = [None]*10
for i in range(n):
    circle[i] = plt.Circle((x0[i], y0[i]), R[i], color='k', fill=False)
    ax.add_artist(circle[i])

plt.xlabel (r'$x$')
plt.ylabel (r'$y$')
#plt.colorbar ( imgplot, orientation='horizontal' )
plt.savefig("./1dipol1_1.png")
plt.show ()

print (time.time() - start, "g")
