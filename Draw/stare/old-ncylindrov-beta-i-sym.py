import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

data = np.load("./Results/ncylindrov2.npz")
frequencies=data['frequencies']
alpha=data['alpha']
beta=data['beta']
mmax=alpha.shape[2]//2
gama=data['gama']
a=data['a']
mrow=data['mrow']

def plotabsbetam (m):
	plt.figure ( figsize = (7,7) )
	plt.plot ( (np.abs (beta[int(frequencies.size/2.2),:,mmax+m])+ np.abs (beta[int(frequencies.size/2.2),:,mmax-m]))/2., '-*b' )
	plt.xlabel (r'$i$')
	plt.ylabel (r'$\|\beta_'+str(m)+r'\|$')
	plt.tight_layout()
	plt.savefig ("./Plots/ncylindrov-beta"+str(m)+"-i-sym.png")
	plt.show()


plotabsbetam (2)
print(mmax)

