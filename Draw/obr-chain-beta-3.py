#beta_m of each m in one picture
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from scipy import special as bessel # we will use only bessel functions
import matplotlib.pyplot as plt
import math

inputName = "21cylindrov"
plotName = "chain-beta-3"

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

idx=np.argmin(np.abs(beta[100:200,10,0+mmax]))+100
print(np.abs(beta[idx,10,0+mmax]))
y1labels=[r'$|\beta_{i\, 0}|$', r'$|\beta_{i\, 1}|$', r'$|\beta_{i\, 2}|$']
y2labels=[r'$\angle\beta_{i\, 0}$', r'$\angle\beta_{i\, 1}$', r'$\angle\beta_{i\, 2}$']

def plotabsbetam (idx):
    plt.figure ( figsize = (10,5) )
    fig, ax = plt.subplots(3,1, sharey=False)

    for m in range(0,3):
        ax1=ax[m]
        ax2 = ax1.twinx()

        #ax1.set_yscale("log")
        j=m+mmax
        ax1.set_ylim(bottom=0, top=max(np.abs( beta[idx,:,j])))
        ax1.plot (  range(n), np.abs( beta[idx,:,j]) , 'o:', label=r'$m=$%d'%(m))
        if m==2:
            ax1.set_xlabel ( r'$i$' )
        ax1.set_ylabel ( y1labels[m] )
        ax1.set_title(r'$m=$ %d,  $f=$%1.2f'%(m, frequencies[idx]))

        ax2.plot (  range(n), np.angle( beta[idx,:,j], deg=1) , 'x:r', label=r'$m=$%d'%(m))
        ax2.set_ylabel ( y2labels[m] )
        ax2.set_ylim(-180,180)
        if m==0:
            plt.title(r"$R=0.45$, $\epsilon=80$", loc="right", x=0.95)

    #plt.suptitle(r"$f=$%f"%(frequencies[idx]))
    plt.tight_layout()
    plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
    #plt.show()

plotabsbetam (idx)
