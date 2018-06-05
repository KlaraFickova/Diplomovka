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

inputName = "21cylindrov"
fileName1 = inputName + "-Efield1"
fileName2 = inputName + "-Efield2"
plotName = "21cyl-Efield-min-vs-max"
data1 = np.load("./Results/"+fileName1+".npz")
data2 = np.load("./Results/"+fileName2+".npz")
inputData = np.load("./Inputs/" + inputName + ".npz")

n = inputData['n']
R = inputData['R']
x0 = inputData['x']
y0 = inputData['y']

E1       = data1['E']
E2       = data2['E']
f1      = data1['f']
f2      = data2['f']
Xleft   = data1["Xleft"]
Xright  = data1["Xright"]
Ydown   = data1["Ydown"]
Yup     = data1["Yup"]

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

print (time.time() - start, "arrays loaded")

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


plt.figure ( figsize = (10, 10) )
fig, ax = plt.subplots(2,2, gridspec_kw = {'height_ratios':[3.5, 1]})
print(ax.shape)

ColorE = Complex2RGB(E1, 0., 2.)
imgplot1 = ax[0,0].imshow ( ColorE,  extent = [ Xleft, Xright, Ydown, Yup ], origin = 'lower' , interpolation = 'gaussian' )

#ax[0,0]=ax[0,0].gca()
circle = np.array( [ plt.Circle((x0[i], y0[i]), R[i], color='r', fill=False)  for i in range(n) ] ).reshape(-1)
#circle = np.array([[plt.Circle((x0[2*i], y0[2*i]), R[2*i], color='r', fill=False) , plt.Circle((x0[2*i+1], y0[2*i+1]), R[2*i+1], color='b', fill=False)]  for i in range(n//2)]).reshape(-1)
for i in range(n):
    ax[0,0].add_artist(circle[i])

ax[0,0].set_xlabel (r'$x$')
ax[0,0].set_ylabel (r'$y$')
ax[0,0].set_title (r'$f = $%4.2f'%(f1) + r', $N=21$, $R=0.45$, $\epsilon=80$')


ColorE = Complex2RGB(E2, 0., 2.)
imgplot = ax[0,1].imshow ( ColorE,  extent = [ Xleft, Xright, Ydown, Yup ], origin = 'lower' , interpolation = 'gaussian' )

#ax[0,1]=plt.gca()
circle = np.array( [ plt.Circle((x0[i], y0[i]), R[i], color='r', fill=False)  for i in range(n) ] ).reshape(-1)
#circle = np.array([[plt.Circle((x0[2*i], y0[2*i]), R[2*i], color='r', fill=False) , plt.Circle((x0[2*i+1], y0[2*i+1]), R[2*i+1], color='b', fill=False)]  for i in range(n//2)]).reshape(-1)
for i in range(n):
    ax[0,1].add_artist(circle[i])

ax[0,1].set_xlabel (r'$x$')
#ax[0,1].set_ylabel (r'$y$')
ax[0,1].set_title (r'$f = $%4.2f'%(f2))

countY1, countX1 = E1.shape

ax[1,0].set_ylim((0,2.5))
ax[1,0].plot(np.linspace(Ydown, Yup, countY1), np.abs(E1[:,countX1//2]))
ax[1,0].set_ylabel(r"$|E|$")
ax[1,0].set_xlabel(r"$y$")

countY2, countX2 = E2.shape

ax[1,1].set_ylim((0,2.5))
ax[1,1].plot(np.linspace(Ydown, Yup, countY2), np.abs(E2[:,countX2//2]))
#ax[1,1].set_ylabel(r"$|E|$")
ax[1,1].set_xlabel(r"$y$")


#plt.colorbar ( imgplot, orientation='horizontal' )
plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
#plt.show ()

print (time.time() - start, "g")
