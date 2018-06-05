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

inputName = "1dipol1"
fileName = inputName + "-Efield5"
plotName = fileName + "-blueGreen2"
data = np.load("./Results/"+fileName+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n = inputData['n']
R = inputData['R']
x0 = inputData['x']
y0 = inputData['y']
epsilon = inputData['epsilon']

E       = data['E']
f       = data['f']
Xleft   = data["Xleft"]
Xright  = data["Xright"]
Ydown   = data["Ydown"]
Yup     = data["Yup"]

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

print (time.time() - start, "arrays loaded")

'''def Complex2HSV(z, rmin, rmax, hue_start=90):
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
'''

def Complex2RGB (z, rmin, rmax) :
    # set middle color
    dhue = 20.
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

plt.figure ( figsize = (7, 5) )
ColorE = Complex2RGB(E, 0., 1000.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft, Xright, Ydown, Yup ], origin = 'lower' , interpolation = 'gaussian' )

ax=plt.gca()
circle = np.array( [ plt.Circle( (x0[i], y0[i]), R[i], color=decideColor(epsilon[i]), fill=False )  for i in range(n) ] ).reshape(-1)
#circle = np.array( [ plt.Circle((x0[i], y0[i]), R[i], color='r', fill=False)  for i in range(n) ] ).reshape(-1)
#circle = np.array([[plt.Circle((x0[2*i], y0[2*i]), R[2*i], color='r', fill=False) , plt.Circle((x0[2*i+1], y0[2*i+1]), R[2*i+1], color='b', fill=False)]  for i in range(n//2)]).reshape(-1)
for i in range(n):
    ax.add_artist(circle[i])

plt.xlabel (r'$x$')
plt.ylabel (r'$y$')
plt.title (r'$f = $'+str(float(f)))
#plt.colorbar ( imgplot, orientation='horizontal' )
plt.savefig("./"+plotName+".pdf", bbox_inches='tight')
#plt.show ()

print (time.time() - start, "g")
