#alpha_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "1cylinder3"
plotName = inputName+"alpha1m"

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

def plotabsalpham (i):
    plt.figure ( figsize = (7,7) )
    plt.yscale("log")
    for j in range(mmax,mmax+11):
        plt.plot (  frequencies, np.abs( alpha[:,i,j]) , '-' )
    plt.xlabel ( r'$i$' )
    plt.ylabel ( r'$abs(\alpha_' + str(i) + r')$' )
    plt.tight_layout()
    plt.savefig("./"+plotName+"-"+str(i)+".png")
    #plt.show()

plotabsalpham (0)
