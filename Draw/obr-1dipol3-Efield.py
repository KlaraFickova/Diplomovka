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

inputName = "1dipol3"
fileName1 = inputName + "-Efield1"
fileName2 = inputName + "-Efield2"
plotName = "1dipol3-Efield"
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n = inputData['n']
R = inputData['R']
x0 = inputData['x']
y0 = inputData['y']
epsilon = inputData['epsilon']

E1       = data1['E']
E2       = data2['E']
f       = data1['f']
Xleft1   = data1["Xleft"]
Xright1  = data1["Xright"]
Ydown1   = data1["Ydown"]
Yup1     = data1["Yup"]
Xleft2   = data2["Xleft"]
Xright2  = data2["Xright"]
Ydown2   = data2["Ydown"]
Yup2     = data2["Yup"]

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

print (time.time() - start, "arrays loaded")

def Complex2RGB (z, rmid) :
    # set middle color
    dhue = 20.
    hue_start = 180.-dhue
    # get amplidude of z and limit to [rmin, rmax]
    amp = np.abs(z)
    h = hue_start + np.where(amp, dhue * (np.real(z) / amp), 0) 		#hue = 120° - 180°
    s = amp / rmid
    s = np.where (s < 0, 0., s)
    s = np.arctan(s)/pi *2
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

plt.figure ( figsize = (10, 5.5) )
plt.subplot(1,2,1)
ColorE = Complex2RGB(E1, 5.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft1, Xright1, Ydown1, Yup1 ], origin = 'lower' , interpolation = 'gaussian' )

ax=plt.gca()
circle = np.array( [ plt.Circle( (x0[i], y0[i]), R[i], color=decideColor(epsilon[i]), fill=False )  for i in range(n) ] ).reshape(-1)
for i in range(n):
    ax.add_artist(circle[i])

plt.xlabel (r'$x$')
plt.ylabel (r'$y$')
plt.title (r'$f = 0.838$, $r_{mid}=5$, $R=0.45$, $\epsilon = (1.1 \pm 0.1\mathrm{i})^2$')


plt.subplot(1,2,2)
ColorE = Complex2RGB(E2, 100.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft2, Xright2, Ydown2, Yup2 ], origin = 'lower' , interpolation = 'gaussian' )

ax=plt.gca()
circle = np.array( [ plt.Circle( (x0[i], y0[i]), R[i], color=decideColor(epsilon[i]), fill=False )  for i in range(n) ] ).reshape(-1)
for i in range(n):
    ax.add_artist(circle[i])

plt.xlabel (r'$x$')
plt.title (r'$r_{mid}=100$')

plt.tight_layout()
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')

print (time.time() - start, "g")
