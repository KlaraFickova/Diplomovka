#beta_m of each cylinder in one picture
import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "dipoleHexaNet3"

data = np.load("./Results/"+inputName+".npz")
data.updtate(np.load("./Inputs/"+inputName+".npz"))
frequencies=data['frequencies']
alpha=data['alpha']			#alpha[f,n,m]
beta=data['beta']			#beta[f,n,m]
n=alpha.shape[1]
mmax=alpha.shape[2]//2
gama=data['gama']
a=data['a']
mrow=data['mrow']

def plotabsbetam (m):
	plt.figure ( figsize = (7,7) )
	for i in range (n):
		plt.plot (  frequencies, np.abs( beta[:,i,m] ), '-' )
	plt.xlabel ( r'$i$' )
	plt.ylabel ( r'$abs(\beta_' + str(m) + r')$' )
	plt.tight_layout()
	#plt.savefig ("1-alpharealimag-m"+str(m)+".png")
	plt.show()


plotabsbetam (1)
