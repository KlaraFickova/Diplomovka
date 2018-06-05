import numpy as np
from numpy import pi
from scipy import special as bessel # we will use only bessel functions
import matplotlib as mpl



axis = np.linspace(2*pi*0.5*0.45,10,100)

for m in range(11):
	maxim = np.max(np.abs(bessel.hankel1 ( m, axis)))
	print(m, ': ', maxim)
