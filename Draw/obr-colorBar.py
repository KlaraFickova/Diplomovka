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

plotName = "colorBar"

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

def Complex2RGB (z, rmin, rmax) :
    # set middle color
    dhue = 15.
    hue_start = 180.-dhue
    # get amplidude of z and limit to [rmin, rmax]
    amp = np.abs(z)
    h = hue_start + np.where(amp, dhue * (np.real(z) / amp), 0) 		#hue = 120° - 180°
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

def decideColor(epsilon):
    if np.imag(epsilon) >=0:
        return 'r'
    else:
        return 'b'


plt.figure ( figsize = (7, 1.6) )

plt.subplot(2,1,1)
E       = np.empty((2,101), dtype=np.complex128)
E[0,:]  = (np.linspace(0,2,101)*1j).reshape((1,-1))
E[1,:]  = (np.linspace(0,2,101)).reshape((1,-1))
Xleft   = 0
Xright  = 2
ColorE = Complex2RGB(E, 0., 2.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft, Xright, 0, Xright/20 ], origin = 'lower' , interpolation = 'gaussian' )

plt.xticks([0., 0.5, 1., 1.5, 2.], (r'$|E|=0$', r'$0.5$', r'$1$', r'$1.5$', r'$\geq 2$'))
plt.yticks([])

plt.subplot(2,1,2)
E       = 2*np.exp( 1j* np.linspace(0,2*pi,101) )
Xleft   = 0
Xright  = 2
ColorE = Complex2RGB(E, 0., 2.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft, Xright, 0, Xright/20 ], origin = 'lower' , interpolation = 'gaussian' )

plt.xticks([0., 0.5, 1., 1.5, 2.], (r'$\angle E=0\pi$', r'$\pi/2$', r'$\pi$', r'$1.5\pi$', r'$2\pi$'))
plt.yticks( [] )

plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()

print (time.time() - start, "g")
