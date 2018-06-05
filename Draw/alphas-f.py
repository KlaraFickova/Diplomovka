#beta_m of each cylinder in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "dipoleHexaNet3"
plotName = inputName+"-alphas-f"

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

def plotabsalpham (m):
    plt.figure ( figsize = (7,7) )
    plt.yscale("log")
    for i in range (n):
        plt.plot (  frequencies, np.abs( alpha[:,i,m]), '-' )
    plt.xlabel ( r'$i$' )
    plt.ylabel ( r'$abs(\alpha_' + str(m) + r')$' )
    plt.tight_layout()
    plt.savefig("./"+plotName+"-"+str(m)+".png")
    #plt.show()

plotabsalpham (1)
