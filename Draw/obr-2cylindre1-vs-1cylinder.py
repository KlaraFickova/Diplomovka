#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "1cylinder2"
inputName2 = "2cylindre1"
plotName = inputName2 + "-vs-1cylinder"

data = np.load("./Results/"+inputName+".npz")
data2 = np.load("./Results/"+inputName2+".npz")
inputData=np.load("./Inputs/"+inputName+".npz")
inputData2=np.load("./Inputs/"+inputName2+".npz")

frequencies=inputData['frequencies']
alpha=data['alpha']			#alpha[f,n,m]
beta=data['beta']			#beta[f,n,m]
n=inputData['n']
beta2=data2['beta']
mmax=inputData['mmax']
mmax2=inputData2['mmax']
gama=inputData['gama']
a=inputData['a']
mrow=inputData['mrow']
R=inputData['R']

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'

def plotabsbetam (i):
    plt.figure ( figsize = (10,6) )
    #plt.yscale("log")
    #plt.ylim(1e-4,1e1)

    plt.subplot(3,1,1)
    plt.title(r"$m=0$")
    plt.title(r"$R=0.45$, $\epsilon=80$", loc="left", x=0.05)
    for m in [0]:
        j=m+mmax
        j2=m+mmax2
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', label=r"$N=1$")
        plt.plot (  frequencies, np.abs( beta2[:,i,j2]) , '-', label=r"$N=2$, $i=0$" )
        plt.plot (  frequencies, np.abs( beta2[:,i+1,j2]) , '-', label=r"$N=2$, $i=1$" )
    plt.ylabel ( r'$|\beta_{i\,0}| $' )
    plt.legend(loc="upper right", bbox_to_anchor=(1, 1.2), ncol=3)

    plt.subplot(3,1,2)
    plt.title(r"$m=1$")
    for m in [1]:
        j=m+mmax
        j2=m+mmax2
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', label=r"$N=1$")
        plt.plot (  frequencies, np.abs( beta2[:,i,j2]) , '-', label=r"$N=2, i=0$" )
        plt.plot (  frequencies, np.abs( beta2[:,i+1,j2]) , '-', label=r"$N=2, i=1$" )
    plt.ylabel ( r'$|\beta_{i\,1}| $' )

    plt.subplot(3,1,3)
    plt.title(r"$m=-1$")
    for m in [-1]:
        j=m+mmax
        j2=m+mmax2
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', label=r"$N=1$")
        plt.plot (  frequencies, np.abs( beta2[:,i,j2]) , '-', label=r"$N=2, i=0$" )
        plt.plot (  frequencies, np.abs( beta2[:,i+1,j2]) , '-', label=r"$N=2, i=1$" )
    plt.xlabel ( r'$f$' )
    plt.ylabel ( r'$|\beta_{i\,\, -1}| $' )

    plt.tight_layout()
    plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
    #plt.show()

plotabsbetam (0)
