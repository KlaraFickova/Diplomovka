#beta -1, 0 and 1 for 1 cylinder - absolute value, real part, imaginary part
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "1cylinder0"
plotName = "betas-re-im-abs"

data = np.load("./Results/"+inputName+".npz")
inputData=np.load("./Inputs/"+inputName+".npz")
frequencies=inputData['frequencies']
alpha=data['alpha']			#alpha[f,n,m]
beta=data['beta']			#beta[f,n,m]
n=inputData['n']
mmax=inputData['mmax']
gama=inputData['gama']
a=inputData['a']
mrow=inputData['mrow']
R=inputData['R']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'
print(mpl.rcParams)

def plotbetam (i):
    plt.figure ( figsize = (10,7) )
    #plt.yscale("log")
    #plt.ylim(1e-10,1e1)
    plt.subplot(3,1,1)
    plt.title (r'$R=0.45$, $\epsilon=80$')
    for m in range(-1,2):
        j=m+mmax
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', label=r'$m=$ %d'%(m) )
    plt.ylabel ( r'$|\beta_m|$' )
    plt.legend(loc="lower right")

    plt.subplot(3,1,2)
    for m in range(-1,2):
        j=m+mmax
        plt.plot (  frequencies, np.real( beta[:,i,j]) , '-', label=r'$m=$ %d'%(m) )
    plt.ylabel ( r'$\Re(\beta_m)$' )
    plt.legend(loc="lower right")

    plt.subplot(3,1,3)
    for m in range(-1,2):
        j=m+mmax
        plt.plot (  frequencies, np.imag( beta[:,i,j]) , '-', label=r'$m=$ %d'%(m) )
    plt.xlabel ( r'$f$' )
    plt.ylabel ( r'$\Im(\beta_m)$' )
    plt.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
    #plt.show()

plotbetam (0)
