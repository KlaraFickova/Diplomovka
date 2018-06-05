import numpy as np
from numpy import pi
import os

fileName = "1cylinder1"

# Precision integers
mmax = 10
mrow = np.arange(-mmax,mmax+1)
countf = 10001

# Environment variables and constants
frequencies = np.linspace (0, 2, countf)
epsilon = 60.
mi = 1.
zeta = np.sqrt (mi/epsilon)

# Geometry
R = 0.45
x = 0
y = 0

os.system("nano ../Inputs/"+fileName+".txt")
np.savez("./Inputs/"+ fileName +".npz", mmax=mmax, mrow=mrow, countf=countf, frequencies=frequencies, mi=mi, zeta=zeta, epsilon=epsilon, R=R, x=x, y=y)
