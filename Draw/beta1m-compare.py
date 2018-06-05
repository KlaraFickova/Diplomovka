#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "2cylindre2"
inputName2 = "1cylinder2"
plotName = inputName+"-beta1m-compare"

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
    plt.figure ( figsize = (10,7) )
    plt.yscale("log")
    plt.ylim(1e-20,1e1)
    plt.title(r"farebné čiary: $m_{max}=10$, šedo-farebné čiary: $m_{max}=20$ ")
    colors = mpl.colors.hsv_to_rgb([np.array([h,1,0.5]) for h in np.linspace(0,1,11,endpoint=False)])
    colors2 = mpl.colors.hsv_to_rgb([np.array([h,1,1]) for h in np.linspace(0,1,11,endpoint=False)])
    for m in range(0,11):
        j=m+mmax
        j2=m+mmax2
        plt.plot (  frequencies, np.abs( beta[:,i,j]) , '-', color=colors[m],  label=r'$m=$ %d'%(m))
        plt.plot (  frequencies, np.abs( beta2[:,i,j2]) , '-', color=colors2[m], label=r'$m=$ %d'%(m) )
    plt.xlabel ( r'$f$' )
    plt.ylabel ( r'$|\beta_m| $' )
    plt.legend(loc="lower right", ncol=4)
    plt.tight_layout()
    plt.savefig("./"+plotName+".pdf", bbox_inches='tight')
    #plt.show()

plotabsbetam (0)
