#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "21cylindrov"
plotName = inputName+"-beta1m1"

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

idx=100

def plotabsbetam (idx):
    plt.figure ( figsize = (10,5) )
    plt.yscale("log")
    #plt.ylim(-3,3)
    for m in range(0,3):
        j=m+mmax
        plt.plot (  range(n), np.abs( beta[idx,:,j]) , 'o:', label=r'$m=$%d'%(m))
    plt.xlabel ( r'$f$' )
    plt.ylabel ( r'$|\beta_{i m}|$' )
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("./"+plotName+".pdf")
    #plt.show()

plotabsbetam (idx)
