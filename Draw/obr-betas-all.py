#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "1cylinder2"
plotName = "betas-all"

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

def plotabsbetam (i):
    plt.figure ( figsize = (10,6) )
    plt.yscale("log")
    plt.ylim(1e-20,10)
    plt.title(r'$R=0.45$, $\epsilon=80$')
    colors = mpl.colors.hsv_to_rgb([np.array([h,1,1]) for h in np.linspace(0,1,11,endpoint=False)])
    for m in range(0,11):
        j=m+mmax
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', color=colors[m],  label=r'$m=$ %d'%(m))
    plt.xlabel ( r'$f$' )
    plt.ylabel ( r'$|\beta_m| $' )
    plt.legend(loc="lower right", ncol=4)
    plt.tight_layout()
    plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
    #plt.show()

plotabsbetam (0)
