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

inputName = "dipoleHexaNet6"
fileName = inputName + "-Efield7"
plotName = inputName + "-Efield7"
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

plt.figure ( figsize = (7, 7) )
ColorE = Complex2RGB(E, 5.)
imgplot = plt.imshow ( ColorE,  extent = [ Xleft, Xright, Ydown, Yup ], origin = 'lower' , interpolation = 'gaussian' )

ax=plt.gca()
circle = np.array( [ plt.Circle( (x0[i], y0[i]), R[i], color=decideColor(epsilon[i]), fill=False )  for i in range(n) ] ).reshape(-1)
for i in range(n):
    ax.add_artist(circle[i])

plt.xlabel (r'$x$')
plt.ylabel (r'$y$')
plt.title (r'$f = 0.588$, $r_{mid}=5$, $R=0.45$, $\epsilon = (1.1 \pm 0.1\mathrm{i})^2$')
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')

print (time.time() - start, "g")
